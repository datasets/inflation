<a href="https://datahub.io/core/inflation"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25" alt="View on datahub.io" /></a>

Annual inflation rates for countries worldwide, covering two measures: the GDP implicit deflator and consumer prices (CPI). Data is sourced from the World Bank and covers most countries from the 1960s onward.

## Data

There are two data files:

- `data/inflation-gdp.csv` — GDP deflator inflation (`NY.GDP.DEFL.KD.ZG`): annual percentage change of the GDP implicit deflator.
- `data/inflation-consumer.csv` — Consumer price inflation (`FP.CPI.TOTL.ZG`): annual percentage change in consumer prices.

Both files have columns: `Country`, `Country Code`, `Year`, `Inflation`. Rows are omitted for country-years where the World Bank reports no value.

The data is downloaded from the World Bank API:

- [GDP deflator (NY.GDP.DEFL.KD.ZG)](https://api.worldbank.org/v2/en/indicator/NY.GDP.DEFL.KD.ZG?downloadformat=csv)
- [Consumer prices (FP.CPI.TOTL.ZG)](https://api.worldbank.org/v2/en/indicator/FP.CPI.TOTL.ZG?downloadformat=csv)

## Preparation

### Requirements

- Python 3

### Processing

Run the following to download and process the data:

```bash
make data
```

## Automation

Up-to-date (auto-updates every 3 months) inflation dataset could be found on datahub.io:
https://datahub.io/core/inflation

## License

The source data is published by the World Bank under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) license. This data package is accordingly licensed under CC BY 4.0. Attribution: The World Bank.
