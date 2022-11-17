from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import csv

spark = SparkSession.builder.appName('StockSummary').getOrCreate()

googleDF = spark.read.options(inferSchema='True', delimiter=',', header='True').csv('ratings.csv')

type1 = googleDF.filter(col('rating') < 1)
type1.show()
