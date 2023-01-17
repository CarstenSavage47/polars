import polars
from datetime import datetime, timedelta
import numpy as np
import pandas
import pyarrow

iris = polars.read_csv("/Users/carstenjuliansavage/Desktop/R Working Directory/Useful Datasets/iris.csv")

iris.columns

q = (
    iris
    # The asteriks stands for all columns.
    .select(polars.col('*'))
    .filter(polars.col("SepalLength") > 5)
    .groupby("Species")
    .agg(polars.all().sum())
)

q.head(5)

iris.describe()

q.write_csv("/Users/carstenjuliansavage/Documents/q.csv")

