import pandas as pd

## Load in air quality data set from raw data file (https://github.com/pandas-dev/pandas/blob/main/doc/data/air_quality_no2.csv)
air_quality = pd.read_csv("./data/raw-no2-data.csv", index_col=0, parse_dates=True)

## Print top 5 rows of data set
## print(air_quality.head())

## Create a new column from existing column
## air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882

## Check ratio of values in Paris versus Antwerp, save the result as a new column
air_quality["ratio_paris_antwerp"] = (air_quality["station_paris"] / air_quality["station_antwerp"])

print(air_quality.head())
