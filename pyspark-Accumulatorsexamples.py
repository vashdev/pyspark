"""SimpleApp.py"""

from pyspark.sql import SparkSession
#from pyspark.accumulators import AccumulatorParam
from pyspark import AccumulatorParam
spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
sc = spark._sc


class DictParam(AccumulatorParam):
    def zero(self,  value ={}):
        return value

    def addInPlace(self, value1, value2):
        value1.update(value2)  #new item gets uppended
        return value1

class StringAccumulator(AccumulatorParam):
    def zero(self, s):
        return s
    def addInPlace(self, s1, s2):
        return s1 + s2

class FooAccumulator(AccumulatorParam):
        def zero(self, f):
            return []

        def addInPlace(self, acc, el):
            acc.extend(el)
            return acc

#def file_read(dict1,achar):
    #dict1[achar]=dict1[achar]+1  # accumilator not subscriptble

#    return dict1[achar]

logFile = "/Users/akula/README.md"  # Should be some file on your system
dict1=sc.accumulator({}, DictParam())

logData = spark.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('a'))
numBs = logData.filter(logData.value.contains('b'))
numAs.show(2)
#numAsmap = numAs.map(lambda x: file_read(dict1, x)).cache() DF dosent have  map fucntion
numAsmap=numAs.select("value").rdd.map(lambda x: file_read(dict1, x)).cache()
print(f"typeof =  {numAsmap}")
print(numAsmap.collect())




#print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

spark.stop()
