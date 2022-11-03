from pyspark import SparkConf, SparkContext
import sys
import re

conf = SparkConf().setAppName('DistributedGrep')
sc = SparkContext(conf = conf)

sc.textFile(sys.argv[2])\
  .flatMap(lambda line: re.sub(r'\W+', ' ', line).split())\
  .filter(lambda word: (word.lower() == sys.argv[1], word))\
  .map(lambda line: line)\
  .reduceByKey(lambda a: a)\
  .saveAsTextFile("output.txt")

