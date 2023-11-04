"""SimpleApp.py"""
from pyspark.sql import SparkSession

#def getLen(row):


logFile = "/Users/akula/README.md"  # Should be some file on your system
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
logData = spark.read.text(logFile)
print(f" type for cachelog {type(logData)}")
numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

spark.stop()
