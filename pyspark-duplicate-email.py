"""SimpleApp.py"""
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.functions import avg
from pyspark.sql import functions as F
from pyspark.sql.functions import col, explode, posexplode, collect_list, monotonically_increasing_id
from pyspark.sql import Window, types

spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
# find the conseq value repeating 3 times
# Person table:
# +----+---------+
# | id | email   |
# +----+---------+
# | 1  | a@b.com |
# | 2  | c@d.com |
# | 3  | a@b.com |
# +----+---------+
# +----+-----+

df = spark.createDataFrame([
    Row(id=1, email='a@b.com'),Row(id=2, email='c@d.com'),Row(id=3, email='c@d.com')
])
df2=df.groupBy("email").count()

df2.filter("count > 1").show()

spark.stop()
