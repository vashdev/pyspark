"""SimpleApp.py"""
from pyspark.sql import SparkSession
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, desc,sum
from pyspark import SparkContext, SparkConf
from pyspark.accumulators import AccumulatorParam
# Create a Spark session
#spark = SparkSession.builder.appName("WordCount").getOrCreate()
logFile = "/Users/akula/README.md"  # Should be some file on your system
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
logData = spark.read.text(logFile)

# Read text data or create an RDD from a list of strings

logData.createOrReplaceTempView("logtbl")
df1=spark.sql("  select  words from ( SELECT explode(split(value, ' ')) as words  from logtbl) X ")
#mix and match
#print(sorted(df1.groupBy('words').count().collect()))  --> this WORKS
df2=df1.groupBy('words').count()
df2.show()






