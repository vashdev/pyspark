"""SimpleApp.py"""
from pyspark.sql import SparkSession
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, desc
from pyspark import SparkContext, SparkConf
from pyspark.accumulators import AccumulatorParam
from operator import add

logFile = "/Users/akula/README.md"  # Should be some file on your system
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
logData = spark.read.text(logFile)
counts = logData.rdd.flatMap(lambda rec: rec.value.split(" ")) \
                   .map(lambda x:  (x, 1)) \
                   .reduceByKey(add)
print(counts.collect())

#Dataframe
logData.agg('value')


