from pyspark.sql import SparkSession
from pyspark.sql.functions import year
import sys 
import csv

spark = SparkSession.builder.appName('StockSummary').getOrCreate()

googleDF = spark.read.options(inferSchema='True', delimiter=',', header='True').csv(sys.argv[1])

#googleDF.withColumn('Year',year(googleDF.Date)).select('Year', 'Close').groupBy('Year').avg('Close').show()

googleDF.groupBy(year(googleDF.Date)).avg('Close').show()
