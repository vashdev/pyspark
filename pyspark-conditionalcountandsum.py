"""SimpleApp.py"""
from pyspark.sql import SparkSession, Window, types, filter
from pyspark.sql import Row
from pyspark.sql.functions import avg, sum, count
from pyspark.sql.functions import avg, sum,cumsum
#simple running total are so hard without rollup fucntion
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
# id   | country | state    | amount | trans_date |
# +------+---------+----------+--------+------------+
# | 121  | US      | approved | 1000   | 2018-12-18 |
# | 122  | US      | declined | 2000   | 2018-12-19 |
# | 123  | US      | approved | 2000   | 2019-01-01 |
# | 124  | DE      | approved | 2000   | 2019-01-07 |
# +------+---------+----------+--------+------------+
# Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.
#
# Return the result table in any order.


df = spark.createDataFrame([
    Row(id=121, country='USA',state='approved',amount=1000,trans_date='2018-12-18'),
    Row(id=122, country='USA', state='approved', amount=1000, trans_date='2018-12-18'),
    Row(id=123, country='USA', state='approved', amount=1000, trans_date='2018-12-18'),
    Row(id=124, country='DE', state= 'approved', amount=1000, trans_date='2018-12-18')

])
total=df.groupBy([df.country,df.trans_date]).count()
df.groupBy([df.country,df.trans_date]).agg(
    count(lit(1)).alias('total_rec'),
    count(when(col("state") == "approved", 1)).alias('approved_count'),
     sum(when(col("state")=="approved",col("amount")) ).alias("approval_amount"),
sum(when(col("state")=="approved",col("amount")) ).alias("approval_amount")
).collect()

