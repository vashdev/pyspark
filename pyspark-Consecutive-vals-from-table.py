"""SimpleApp.py"""
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.functions import avg
from pyspark.sql import functions as F
from pyspark.sql.functions import col, explode, posexplode, collect_list, monotonically_increasing_id
from pyspark.sql import Window, types

spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
# find the conseq value repeating 3 times
# Logs table:
# +----+-----+
# | id | num |
# +----+-----+
# | 1  | 1   |
# | 2  | 1   |
# | 3  | 1   |
# | 4  | 2   |
# | 5  | 1   |
# | 6  | 2   |
# | 7  | 2   |
# +----+-----+

df = spark.createDataFrame([
    Row(id=1, num=1),Row(id=2, num=1),Row(id=3, num=1),Row(id=4, num=2),Row(id=5, num=1),Row(id=6, num=2),
    Row(id=7, num=2)
])

w = Window.orderBy(F.asc("id"))
df=df.withColumn('previous', F.lead('num').over(w))
df=df.withColumn('next', F.lag('num').over(w))

#give rownums
df.filter(  (df.num == df.previous )  & (df.previous   == df.next) ).show()

spark.stop()
