"""SimpleApp.py"""
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.functions import avg
import pandas as pd
from pyspark.sql.functions import col, explode, posexplode, collect_list, monotonically_increasing_id
#https://medium.com/bluekiri/check-your-pyspark-abilities-by-solving-this-quick-challenge-86f563a343dd

#replace filight numbers with name
import re
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
logFile = "/Users/akula/README.md"  # Should be some file on your system
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
logData = spark.read.text(logFile)
word="spark"
#value col has rec
# we need ot break the line into individual word


words= logData.rdd.map(lambda rec: re.findall(word,rec.value)).collect()
print(words)
spark.stop()
