"""SimpleApp.py"""
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.functions import avg

spark = SparkSession.builder.appName("SimpleApp").getOrCreate()

df = spark.createDataFrame([
    Row(p=100, r=4),Row(p=100, r=5),Row(p=100, r=5),
    Row(p=200, r=1),Row(p=100, r=2),Row(p=100, r=1)
])
average_ratings = df.groupBy("p").agg(avg("r").alias("avg_rating"))
finaldf=df.join(average_ratings, df.p == average_ratings.p , 'inner')
ff=finaldf.orderBy('avg_rating').take(2)
print(ff)  # its a list
df.createTempView("products")
df2=spark.sql("select * from products  inner join (select p, AVG(r) as sqlavg  from products group by p) x on products.p=x.p ")
print("show me sql soln")
df2.show()
spark.stop()
