<a href="https://datahub.io/core/inflation"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25)" alt="badge" /></a>

Inflation, GDP deflator (annual %) and Inflation, consumer prices (annual %) for most countries in the world when it has been measured. 

## Data

The data comes from [The World Bank (CPI)](http://api.worldbank.org/indicator/NY.GDP.DEFL.KD.ZG?format=csv), [The World Bank (GDP)](http://api.worldbank.org/indicator/FP.CPI.TOTL.ZG?format=csv)  and is collected from 1973 to 2014. There are some values missing from data so users of the data will have to *guess* what should be in the empty slots.

The actual download happens via [The World Bank's API (with csv as the requested format) (CPI)](http://api.worldbank.org/indicator/FP.CPI.TOTL.ZG?format=csv), [The World Bank's API (with csv as the requested format) (GDP)](http://api.worldbank.org/indicator/NY.GDP.DEFL.KD.ZG?format=csv).

## Preparation

They are parsed via the script **process.py** located in scripts.

## License

This Data Package is licensed by its maintainers under the [Public Domain Dedication and License (PDDL)](http://opendatacommons.org/licenses/pddl/1.0/).