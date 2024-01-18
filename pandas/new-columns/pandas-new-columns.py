import pandas as pd

## Load in air quality data set from raw data file (https://github.com/pandas-dev/pandas/blob/main/doc/data/air_quality_no2.csv)
air_quality = pd.read_csv("./data/raw-no2-data.csv", index_col=0, parse_dates=True)

## Print top 5 rows of data set
## print(air_quality.head())

## Create a new column from existing column
## air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882

## Check ratio of values in Paris versus Antwerp, save the result as a new column
air_quality["ratio_paris_antwerp"] = (air_quality["station_paris"] / air_quality["station_antwerp"])

## Rename data colunmns to corresponsing station identifiers used by OpenAQ:
## The rename() function can be used for both row labels and column labels. Provide a dictionary with the keys the current names and the values the new names to update the corresponding names.
air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)

# print top 5 rows of renamed data set
print(air_quality_renamed.head())

# print top 5 rows of data set
print(air_quality.head())

## Notes:
    ## Create a new column by assigning the output to the DataFrame with a new column name in between the [].

    ## Operations are element-wise, no need to loop over rows.

    ## Use rename with a dictionary or function to rename row labels or column names.

