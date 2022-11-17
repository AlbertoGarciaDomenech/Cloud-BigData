from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import csv

spark = SparkSession.builder.appName('StockSummary').getOrCreate()

googleDF = spark.read.options(inferSchema='True', delimiter=',', header='True').csv("Meteorite_Landings.csv")

#lo mostramos por pantalla
googleDF.filter(col('mass (g)').isNotNull()).groupBy('recclass').avg('mass (g)').show()
#lo guardamos en un archivo .csv
googleDF.filter(col('mass (g)').isNotNull()).groupBy('recclass').avg('mass (g)').write.csv('output.csv')