"""SimpleApp.py"""
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.functions import avg
from pyspark.sql import functions as F
from pyspark.sql.functions import col, explode, posexplode, collect_list, monotonically_increasing_id
from pyspark.sql import Window, types

spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
# Nth Higest salary
df = spark.createDataFrame([
    Row(p=1, s=40000),Row(p=2, s=5000),Row(p=3, s=3000),Row(p=3, s=3000),Row(p=4, s=4000)
])
N=2
w = Window.orderBy(F.desc("s"))
df=df.withColumn('ranked_sal', F.dense_rank().over(w))
df=df.withColumn('rownuml', F.row_number().over(w))

#give rownums
df.filter(df.rownuml ==N).show()

spark.stop()
