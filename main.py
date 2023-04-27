import polars
from datetime import datetime, timedelta
import numpy as np
import pandas
# pip install xlsx2csv

iris = polars.read_csv(
    "/Users/carstenjuliansavage/Desktop/R Working Directory/Useful Datasets/iris.csv"
)

Analytics_mindset_case_studies_Bank_Investment_Portfolios = polars.read_excel(
    "/Users/carstenjuliansavage/PycharmProjects/Random_Project/Data Files/"
    "Analytics_mindset_case_studies_Bank_Investment_Portfolios.xlsx"
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

df = polars.from_pandas(iris_transformed_pd)

ndistinct_counts = iris.select(
    [
        polars.col("SepalLength").n_unique().alias("SepalLength_ndistinct"),
        polars.col("SepalWidth").unique().count().alias("SepalWidth_ndistinct"),
    ]
)
print(ndistinct_counts)

iris_summary_stats = iris.select(
    [
        polars.sum("SepalLength").alias("sum"),
        polars.min("SepalLength").alias("min"),
        polars.max("SepalLength").alias("max"),
        polars.col("SepalLength").max().alias("other_max"),
        polars.std("SepalLength").alias("std dev"),
        polars.var("SepalLength").alias("variance"),
    ]
)
print(iris_summary_stats)

virginica_only = (
    iris.lazy().filter(polars.col("Species").str.contains(r"gin")).collect()
)
print(virginica_only)
