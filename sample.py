# Databricks notebook source
print("ok")

# COMMAND ----------

import sys
import os
from pyspark.sql.functions import *
sys.path.append(os.path.abspath('..'))

# COMMAND ----------
from helloworld import hello_world
hello_world()

# COMMAND ----------
# script_dir = os.getcwd() #<-- absolute dir the script is in
# rel_path = "sample/data/sample_user_data.csv"
# abs_file_path = os.path.join(script_dir, rel_path)
df = spark.read.format('csv').options(header='true', inferSchema='true').load(f"file:{os.getcwd()}/data/sample_user_data.csv")
print(df.select(col("name")).first.getString(0))
