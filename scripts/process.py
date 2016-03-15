#!/usr/bin/env python
# -*- encoding: utf-8 -*-

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

import sys
import csv
import urllib
import os

# API URL's for inflation information from The World Bank (in csv format)
SOURCES = ['http://api.worldbank.org/indicator/NY.GDP.DEFL.KD.ZG?format=csv', 'http://api.worldbank.org/indicator/NY.GDP.DEFL.KD.ZG?format=csv']
FILE_NAMES = ['inflation-consumer.csv', 'inflation-gdp.csv']

def get_csv(source):
    """
    Get the inflation data as a CSV. Returns a tuple where the first item
    is the header row and the second item is the rows of the CSV.
    """

    inflation = urllib.urlopen(source)
    csvreader = csv.reader(inflation)
    return (csvreader.next(), csvreader)

def process(headers, rows):
    """
    Generator function to process a row in the source CSV and yield a row
    for the output csv. Rows in source CSV have country and country code in
    the first two columns and then the rest of the columns hold the inflation rate for
    each year (or no value if inflation rate isn't known). The output CSV will hold the
    country, country code, the year, and the inflation value (so we're unwinding the
    columns into rows)
    """
    
    yield ["Country", "Country Code", "Year", "Inflation"]

    for row in rows:
        for index, inflation in enumerate(row[2:]):
            if inflation:
                # We yield the country and the country code then we lookup
                # the corresponding year in the header (we add 2 since we're
                # enumerating from the third column)
                yield row[:2]+[headers[index+2], inflation]

def write_csv(rows, filename = None):
    """
    Write rows to a CSV file. Use default dialect for the CSV. If a file name
    is not provided, but source is, the rows will be printed to standard output
    """
	
    with open('data/' + filename, 'w') as output:
		csvwriter = csv.writer(output)
		for row in rows:
			csvwriter.writerow(row)

if __name__ == "__main__":
	for index in range(len(SOURCES)):
		header, row = get_csv(SOURCES[index])
		write_csv(process(header, row), FILE_NAMES[index])

    	
    
    
    
    
    
