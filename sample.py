# Databricks notebook source
print("ok")

# COMMAND ----------

import sys
import os
sys.path.append(os.path.abspath('..'))

# COMMAND ----------
from helloworld import hello_world
hello_world()
