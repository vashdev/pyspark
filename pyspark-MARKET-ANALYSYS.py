"""SimpleApp.py"""
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("SimpleApp").getOrCreate()

Users = spark.createDataFrame([
Row(user_id=1,join_date='2018-01-01',favorite_brand='Lenovo'),
Row(user_id=2,join_date='2018-02-09',favorite_brand='Samsung'),
Row(user_id=3,join_date='2018-01-19',favorite_brand='LG'),
Row(user_id=4,join_date='2018-05-21',favorite_brand='HP')
])
Orders = spark.createDataFrame([
Row(order_id=1,order_date='2019-01-01',item_id=4,buyer_id=1,seller_id=2),
Row(order_id=2,order_date='2018-08-02',item_id=2,buyer_id=1,seller_id=3),
Row(order_id=3,order_date='2019-08-03',item_id=3,buyer_id=2,seller_id=3),
Row(order_id=4,order_date='2018-08-04',item_id=1,buyer_id=4,seller_id=2),
Row(order_id=5,order_date='2018-08-04',item_id=1,buyer_id=3,seller_id=4),
Row(order_id=6,order_date='2019-08-05 ',item_id=2,buyer_id=2,seller_id=4)
])

def nineteen(x):
    return F.year(to_date(x)) =='2019'

 #Write a solution to find for each user, the join date and the number of orders they made as a
# buyer in 2019.
Orders2=Orders.where(F.year(F.to_date(Orders.order_date)) =='2019').withColumn('user_id',Orders.buyer_id)
df=Users.join(Orders2,'user_id','left_outer')
res=df.groupBy(['user_id','join_date']).agg(F.count(df.order_id)).alias("2019total")
res.show()



