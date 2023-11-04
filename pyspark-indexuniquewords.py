"""SimpleApp.py"""
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.functions import avg
import pandas as pd
from pyspark.sql.functions import col, explode, posexplode, collect_list, monotonically_increasing_id
#https://medium.com/bluekiri/check-your-pyspark-abilities-by-solving-this-quick-challenge-86f563a343dd

#replace filight numbers with name

spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
data = ["This is a sample sentence.", "Another sentence with unique words.", "This is another example."]
rdd = spark.sparkContext.parallelize(data)
# Split the lines into words
words = rdd.flatMap(lambda line: line.split(" "))
#unable to turn this RDD to DF successfull with schema StructType([    StructField('words', StringType(), True)])
#hack
wdf=words.map(lambda x: (x, )).toDF()
wdf=wdf.withColumnRenamed('_1', 'word')


# Remove punctuation and convert words to lowercase (optional)
import string
translator = str.maketrans('', '', string.punctuation)

unique_words = wdf.distinct()
print("show..")
unique_words.show(4)

# wordict= spark.createDataFrame(unique_words, schema = deptSchema)
# wordict.show()
# to make dictionary
wordsdict = unique_words.withColumn("wordId", monotonically_increasing_id())
# dictionary = words.where(trim(words.word) != "").sort(col("wordId").asc())
wordsdict.show(2)
# #Will zip with index work

spark.stop()
