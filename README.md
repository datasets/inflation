Inflation, GDP deflator (annual %) and Inflation, consumer prices (annual %) for most countries in the world when it has been measured. 

# Data

The data comes from [The World Bank (CPI)](http://api.worldbank.org/indicator/NY.GDP.DEFL.KD.ZG?format=csv), [The World Bank (GDP)](http://api.worldbank.org/indicator/FP.CPI.TOTL.ZG?format=csv)  and is collected from 1973 to 2014. There are some values missing from data so users of the data will have to *guess* what should be in the empty slots.

The actual download happens via [The World Bank's API (with csv as the requested format) (CPI)](http://api.worldbank.org/indicator/FP.CPI.TOTL.ZG?format=csv), [The World Bank's API (with csv as the requested format) (GDP)](http://api.worldbank.org/indicator/NY.GDP.DEFL.KD.ZG?format=csv).

They are parsed via the script **inflation2datapackage.py** located in scripts.

## Usage of cpi2datapackage.py

    usage: inflation2datapackage.py [-h] [-o filename] [source]
    
    convert WorldBank CPI data to a data package resource

    positional arguments:
      source                source file to generate output from
    
    optional arguments:
      -h, --help            show this help message and exit
      -o filename, --output filename
                            define output filename
