from pyspark import SparkConf, SparkContext
import sys
import re

conf = SparkConf().setAppName('UrlAccessFrequency')
sc = SparkContext(conf = conf)

sc.textFile(sys.argv[1])\
  .flatMap(lambda line: line.split("\""))\
  .filter(lambda line: "GET" in line or "POST" in line or "HEAD" in line)\
  .map(lambda word: (word.split(" ")[1], 1))\
  .reduceByKey(lambda a, b: a+b)\
  .saveAsTextFile(sys.argv[2])