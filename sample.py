# Databricks notebook source
print("ok")

# COMMAND ----------

import sys
import os
from pyspark.sql.functions import *
#sys.path.append(os.path.abspath('..'))

# COMMAND ----------
df = spark.read.format('csv').options(header='true', inferSchema='true').load(f"file:{os.getcwd()}/data/sample_user_data.csv")
print(df.collect()[0]['name'])

# COMMAND ----------
# MAGIC %scala
# MAGIC import java.io._
# MAGIC val path : String = dbutils.notebook.getContext().notebookPath.get
# MAGIC 
# MAGIC val df = spark.read.format("csv").option("header","true").option("inferSchema", "true").load(s"file:${path}/data/sample_user_data.csv")
# MAGIC println(df.first().getInt(0))

