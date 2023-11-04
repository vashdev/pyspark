"""SimpleApp.py"""
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.functions import avg
from pyspark.sql import functions as F
from pyspark.sql.functions import col, explode, posexplode, collect_list, monotonically_increasing_id
from pyspark.sql import Window, types

spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
# #+--------------+---------+
# | Column Name  | Type    |
# +--------------+---------+
# | id           | int     |
# | name         | varchar |
# | salary       | int     |
# | departmentId | int     |
# +--------------+---------+

df = spark.createDataFrame([
    Row(id=1,salary=7000, departmentId=1),
Row(id=2,salary=9000, departmentId=1),
Row(id=3,salary=8000, departmentId=2),
Row(id=4,salary=6000, departmentId=2),
Row(id=5,salary=9000, departmentId=1)
])
w = Window.partitionBy("departmentId").orderBy(df.salary.desc())

df2= df.withColumn('srank',F.rank().over(w))

df2.filter(df2.srank ==1).show()

spark.stop()
