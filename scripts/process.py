#!/usr/bin/python
# -*- coding: utf-8 -*-

# process.py - convert WorldBank inflation source files to datapackage resource
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import io
import os
import csv
import zipfile
import urllib.request
import itertools

SOURCES = \
    ['https://api.worldbank.org/v2/en/indicator/NY.GDP.DEFL.KD.ZG?downloadformat=csv'
     ,
     'https://api.worldbank.org/v2/en/indicator/FP.CPI.TOTL.ZG?downloadformat=csv'
     ]
FILE_NAMES = ['inflation-consumer.csv', 'inflation-gdp.csv']


def update_archive(source):
    """
    Update the archive with the latest inflation data from The World Bank,
    and skip the first 4 rows in the CSV.
    """
    response = urllib.request.urlopen(source)
    zip_file = zipfile.ZipFile(io.BytesIO(response.read()))
    
    # Find the CSV file that starts with 'API_'
    csv_filename = next(f for f in zip_file.namelist() if f.startswith('API_'))

    new_csv_name = csv_filename.split('_')[1] + '.csv'
    
    with zip_file.open(csv_filename) as csvfile:
        csvreader = csv.reader(io.TextIOWrapper(csvfile, encoding='ISO-8859-1'))
        rows = list(itertools.islice(csvreader, 4, None))  # Skip the first 4 rows
        
        # Save the CSV file to the 'archive' folder with the new name
        with open(os.path.join('archive', new_csv_name), 'w', newline='') as output:
            writer = csv.writer(output)
            writer.writerows(rows)

def get_csv(source):
    """
    Get the inflation data as a CSV from a ZIP file. Returns a tuple where the
    first item is the header row and the second item is the rows of the CSV.
    """

    # Download the ZIP file

    response = urllib.request.urlopen(source)
    zip_file = zipfile.ZipFile(io.BytesIO(response.read()))

    # Find the file that starts with "API_"

    csv_filename = next(f for f in zip_file.namelist()
                        if f.startswith('API_'))

    # Open and read the CSV file

    with zip_file.open(csv_filename) as csvfile:
        csvreader = csv.reader(io.TextIOWrapper(csvfile,
                               encoding='ISO-8859-1'))
        next(csvreader)
        next(csvreader)
        next(csvreader)
        next(csvreader)
        header = next(csvreader)
        return header, list(csvreader)


def process(headers, rows):
    """
    Generator function to process a row in the source CSV and yield a row
    for the output csv. Rows in source CSV have country and country code in
    the first two columns and then the rest of the columns hold the inflation rate for
    each year (or no value if inflation rate isn't known). The output CSV will hold the
    country, country code, the year, and the inflation value (so we're unwinding the
    columns into rows)
    """

    yield ['Country', 'Country Code', 'Year', 'Inflation']

    for row in rows:
        for (index, inflation) in enumerate(row[2:]):
            if inflation and index > 1:

                # We yield the country and the country code then we lookup
                # the corresponding year in the header (we add 2 since we're
                # enumerating from the third column)
                yield row[:2] + [headers[index + 2], inflation]

def write_csv(rows, filename=None):
    """
    Write rows to a CSV file. Use default dialect for the CSV. If a file name
    is not provided, but source is, the rows will be printed to standard output
    """

    with open('data/' + filename, 'w') as output:
        csvwriter = csv.writer(output)
        for row in rows:
            csvwriter.writerow(row)


if __name__ == '__main__':
    for index in range(len(SOURCES)):
        update_archive(SOURCES[index])
        header, row = get_csv(SOURCES[index])
        write_csv(process(header, row), FILE_NAMES[index])
