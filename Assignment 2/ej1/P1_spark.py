from pyspark import SparkConf, SparkContext
import sys

conf = SparkConf().setAppName('DistributedGrep')
sc = SparkContext(conf = conf)
word = sys.argv[1]

sc.textFile(sys.argv[2])\
  .filter(lambda line: word in line)\
  .saveAsTextFile('output.txt')