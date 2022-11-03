from pyspark import SparkConf, SparkContext
import sys
import re

conf = SparkConf().setAppName('UrlAccessFrequency')
sc = SparkContext(conf = conf)

sc.textFile('access_log')\
  .flatMap(lambda line: line.split("\"")[1])\
  .filter(lambda word: ("GET" in word))\
  .filter(lambda word: ("POST" in word))\
  .filter(lambda word: ("HEAD" in word))\
  .map(lambda word: (word.split(" ")[1], 1))\
  .reduceByKey(lambda a, b: a+b)\
  .saveAsTextFile("output3.txt")