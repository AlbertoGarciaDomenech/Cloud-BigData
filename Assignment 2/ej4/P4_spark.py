from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, avg
import csv

spark = SparkSession.builder.appName('StockSummary').getOrCreate()

googleDF = spark.read.options(inferSchema='True', delimiter=',', header='True').csv('ratings.csv')

#parte 1
films = googleDF.groupBy('movieId').avg('rating')

#parte 2
type1 = films.filter(col('avg(rating)') <= 1).select('movieId')
type1.withColumn('Range', lit(1)).show()
type1.write.csv('Range_1.csv')

type2 = films.filter((col('avg(rating)') <= 2) & (col('avg(rating)') > 1)).select('movieId')
type2.withColumn('Range', lit(2)).show()
type2.write.csv('Range_2.csv')

type3 = films.filter((col('avg(rating)') <= 3) & (col('avg(rating)') > 2)).select('movieId')
type3.withColumn('Range', lit(3)).show()
type3.write.csv('Range_3.csv')

type4 = films.filter((col('avg(rating)') <= 4) & (col('avg(rating)') > 3)).select('movieId')
type4.withColumn('Range', lit(4)).show()
type4.write.csv('Range_4.csv')

type5 = films.filter((col('avg(rating)') <= 5) & (col('avg(rating)') > 4)).select('movieId')
type5.withColumn('Range', lit(5)).show()
type5.write.csv('Range_5.csv')