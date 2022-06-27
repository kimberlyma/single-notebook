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

df = spark.read.format('csv').options(header='true', inferSchema='true').load(f"file:{os.getcwd()}/data/sample_user_data.csv")
print(df.collect()[0]['name'])

# COMMAND ----------

df = spark.read.format('csv').options(header='true', inferSchema='true').load(f"file:{os.getcwd()}/data/sample_user_data.csv")
print(df.collect()[0]['name'])

print(inspect.getmodule(read_csv).__name__)
