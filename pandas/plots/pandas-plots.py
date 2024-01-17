import pandas as pd
import matplotlib.pyplot as plt

## Load in air quality data set from raw data file (https://github.com/pandas-dev/pandas/blob/main/doc/data/air_quality_no2.csv)
air_quality = pd.read_csv("./data/raw-no2-data.csv", index_col=0, parse_dates=True)

## Print top 5 rows of data set
print(air_quality.head())

## Visual of data
## air_quality.plot()

## plt.show()

## Plot only columns of data table with data from Paris
## air_quality["station_paris"].plot()

## Show available plot methods

print(air_quality.plot.__doc__)

## Compare NO2 values measured in London and Paris
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)

plt.show()


