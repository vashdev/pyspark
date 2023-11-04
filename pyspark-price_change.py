"""SimpleApp.py"""
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import functions as F
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
spark.conf.set("spark.sql.legacy.timeParserPolicy","LEGACY")

#Write a solution to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10.
#Each row of this table indicates that the price of some product was changed to a new price at some date.
# +------------+-------+
# | product_id | price |
# +------------+-------+
# | 2          | 50    |
# | 1          | 35    |
# | 3          | 10    |
# +------------+-------+
Products = spark.createDataFrame([
Row(product_id=1,new_price=20,change_date='2019-08-14'),
    Row(product_id=2,new_price=50,change_date='2019-08-14'),
    Row(product_id=1, new_price=30, change_date='2019-08-15'),
    Row(product_id=1, new_price=35, change_date=' 2019-08-16'),
    Row(product_id=2, new_price=65, change_date=' 2019-08-17'),
    Row(product_id=3, new_price=20, change_date=' 2019-08-18')

])
 # case 1 price avilable only after 08 16 the price is 10
 # union all for all other recs get latest rec price
Products.createOrReplaceTempView("Products")
df1=spark.sql(" SELECT product_id, 10 AS price FROM Products WHERE  to_date(change_date,'yyyy-MM-dd') > cast('2000-08-16' as date)  GROUP BY product_id     ")
df1=spark.sql(" SELECT product_id,   new_price AS price FROM Products WHERE \
(product_id, change_date) IN ( \
    SELECT  product_id, MAX(change_date) FROM Products WHERE \
      to_date(change_date,'yyyy-MM-dd') < = cast('2000-08-16' as date)  GROUP BY product_id ) ")


df1.show()
