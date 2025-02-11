# %%
from pyspark.sql import SparkSession
import os
import boto3

# %%
#s3_path = "s3a://store-sales-time-series-forecasting/data/raw"
s3_path = "/Users/akhil/Projects/Kaggle/store-sales-time-series-forecasting/data/raw"

# %%
spark = SparkSession.builder \
        .appName("store-sales-time-series-forecasting") \
        .master("local[*]") \
        .getOrCreate()


# %%
train = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(os.path.join(s3_path,"train.csv"))

transactions = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(os.path.join(s3_path,"transactions.csv"))

oil = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(os.path.join(s3_path,"oil.csv"))

holidays_events = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(os.path.join(s3_path,"holidays_events.csv"))

stores = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(os.path.join(s3_path,"stores.csv"))





