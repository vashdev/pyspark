"""SimpleApp.py"""
from pyspark.sql import SparkSession, Window, types
from pyspark.sql import Row
from pyspark.sql.functions import avg, sum,cumsum
#simple running total are so hard without rollup fucntion
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()

df = spark.createDataFrame([
    Row(p=200, r=1),Row(p=100, r=2),Row(p=100, r=3),Row(p=100, r=4),Row(p=100, r=5)
])
window_spec = Window.orderBy("r").rowsBetween(Window.unboundedPreceding, 0) #upto this row in running total

df = df.withColumn("running_total", F.sum("p").over(window_spec))

df.show()
df.createOrReplaceTempView("runTotal")

rt=spark.sql("select distinct t1.r,t1.p,sum(t2.p) OVER (PARTITION BY t1.r  ORDER BY t1.r  ) as runtot  from runTotal t1 inner join runTotal t2 on t1.r>=t2.r" )
#remove partition u get same result

rt.show()