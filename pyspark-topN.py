"""SimpleApp.py"""
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.functions import avg
from pyspark.sql import functions as F
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
#Top users based on duration
df = spark.createDataFrame([
    Row(p=100, r=4),Row(p=100, r=5),Row(p=100, r=5),
    Row(p=200, r=1),Row(p=100, r=2),Row(p=100, r=1),
    Row(p=300, r=1),Row(p=100, r=5),Row(p=100, r=10)
])
maxTimedf = df.groupBy("p").agg(F.sum("r").alias("maxTime"))
finaldf=df.join(maxTimedf, df.p == maxTimedf.p , 'inner')
finaldf.orderBy('maxTime').show()
#pysql
df.createTempView("products")
df2=spark.sql("select * from products  inner join (select p, SUM(r) as sqlmax  from products group by p) x on products.p=x.p ")
print("show me sql soln")
df2.show()
spark.stop()
