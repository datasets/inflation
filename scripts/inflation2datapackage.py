#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# inflation2datapackage.py - convert WorldBank inflation source files to datapackage resource
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

# API URL's for inflation information from The World Bank (in csv format)
sources = ['http://api.worldbank.org/indicator/NY.GDP.DEFL.KD.ZG?format=csv', 'http://api.worldbank.org/indicator/NY.GDP.DEFL.KD.ZG?format=csv']
file_names = ['inflation-consumer.csv', 'inflation-gdp.csv']

def get_csv(source):
    """
    Get the inflation data as a CSV. Returns a tuple where the first item
    is the header row and the second item is the rows of the CSV.
    """

    # Get the CSV (use urllib.urlopen to allow files and urls)
    inflation = urllib.urlopen(source)
    # Create the csv reader
    csvreader = csv.reader(inflation)
    # Return a tuple: (headers, rows)
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

    # First we yield the headers (we hardcode them since at the time of
    # writing the World Bank API source returns a broken header row)
    yield ["Country", "Country Code", "Year", "Inflation"]

    for row in rows:
        # Go through the inflation values in each row (we need the index as well)
        for index, inflation in enumerate(row[2:]):
            # If there is some value for the inflation we yield it
            if inflation:
                # We yield the country and the country code then we lookup
                # the corresponding year in the header (we add 2 since we're
                # enumerating from the third column)
                yield row[:2]+[headers[index+2], inflation]

def write_csv(rows, filename=None):
    """
    Write rows to a CSV file. Use default dialect for the CSV. If a file name
    is not provided, but source is, the rows will be printed to standard output
    """

    # Set the file as stdout if no filename, else open the file for writing
    output = sys.stdout if filename is None else open(filename, 'w')
    # Create the csv writer
    csvwriter = csv.writer(output)
    # Write all the rows
    csvwriter.writerows(rows)
    # Close the output file (or stdout)
    output.close()

if __name__ == "__main__":
    # Define arguments parser
    import argparse
    parser = argparse.ArgumentParser(
        description='convert WorldBank Inflation data to a data package resource')
    # Output file option
    parser.add_argument('-o', '--output', dest='filename', action='store',
                        default=None, metavar='filename',
                        help='define output filename')
    # Source file (default is the global list of inflation URL's)
    parser.add_argument('source', default=sources, nargs='?',
                        help='source file to generate output from')
    # Parse the arguments into args
    args = parser.parse_args()
    if type(args.source) == str:
	# if the link is provided script will retrieve data from link
        # Get the header and the rows
        headers, rows = get_csv(args.source)
        # Process them (this returns a generator)
        processed_rows = process(headers, rows)
        # Write the processed rows to the file
        write_csv(processed_rows, filename=args.filename)
    else:
         # else i not will retrive from both links
         for index in range(len(sources)):
	     # Get the header and the rows
             headers, rows = get_csv(args.source[index])
             # Process them (this returns a generator)
             processed_rows = process(headers, rows)
             # Write the processed rows to the file
             write_csv(processed_rows, file_names[index])
