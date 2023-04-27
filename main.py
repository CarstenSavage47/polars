import polars
from datetime import datetime, timedelta
import numpy as np
import pandas
import pyarrow

iris = polars.read_csv(
    "/Users/carstenjuliansavage/Desktop/R Working Directory/Useful Datasets/iris.csv"
)

iris.columns

iris_all_sums = (
    iris
    # The asteriks stands for all columns.
    .select(polars.col("*"))
    .filter(polars.col("SepalLength") > 5)
    .groupby("Species")
    .agg(polars.all().sum())
)

iris_transformed = iris.select(
    [
        polars.col("*"),
        polars.col("SepalLength").sort().alias("Sorted_SepalLength"),
        polars.col("SepalWidth")
        .filter(polars.col("SepalWidth") > 0)
        .sum()
        .alias("Sum_SepalWidth"),
    ]
).drop(["SepalWidth", "SepalLength"])

iris_transformed_pd = iris_transformed.to_pandas()

ndistinct_counts = iris.select(
    [
        polars.col("SepalLength").n_unique().alias("SepalLength_ndistinct"),
        polars.col("SepalWidth").unique().count().alias("SepalWidth_ndistinct"),
    ]
)
print(ndistinct_counts)

