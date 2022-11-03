from pyspark import SparkConf, SparkContext
import sys
import re
import csv

conf = SparkConf().setAppName('StockSummary')
sc = SparkContext(conf = conf)


path = "/usr/local/spark/examples/src/main/resources/GOOGLE.csv"
googleDF = spark.read.option("header", "true").csv(path)
column_names = next(googleDF)
date = column_names.index("Date")
value = column_names.index("Close")

googleDF.flatMap(lambda line: re.sub(r'\W+', ' ', line).split())\
  .map(lambda word: (word.lower(), 1))\
  .reduceByKey(lambda a, b: a+b)\
  .saveAsTextFile("output.txt")

