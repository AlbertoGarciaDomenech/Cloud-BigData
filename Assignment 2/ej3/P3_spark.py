from pyspark.sql import SparkSession
from pyspark.sql.functions import year 
import csv

spark = SparkSession.builder.appName('StockSummary').getOrCreate()

googleDF = spark.read.options(inferSchema='True', delimiter=',', header='True').csv('GOOGLE.csv')

#googleDF.withColumn('Year',year(googleDF.Date)).select('Year', 'Close').groupBy('Year').avg('Close').show()

#lo mostramos por pantalla
googleDF.groupBy(year(googleDF.Date)).avg('Close').show()
#lo guardamos en un archivo .csv
googleDF.groupBy(year(googleDF.Date)).avg('Close').write.csv('output.csv')