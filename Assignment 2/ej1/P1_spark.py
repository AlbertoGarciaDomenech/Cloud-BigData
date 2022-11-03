from pyspark import SparkConf, SparkContext
import sys
import re

conf = SparkConf().setAppName('DistributedGrep')
sc = SparkContext(conf = conf)
word = sys.argv[1]

sc.textFile(sys.argv[2])\
  .filter(lambda line: word in line)\
  .saveAsTextFile(sys.argv[3])

