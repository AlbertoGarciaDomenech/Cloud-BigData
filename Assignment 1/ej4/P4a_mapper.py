#!/usr/bin/python

import sys
import csv
# abrimos el archivo csv
csvreader = csv.reader(sys.stdin, delimiter =',')
# en la primera linea conseguimos los nombres de las columnas que queremos acceder
column_names = next(csvreader)
_id = column_names.index("movieId")
rating = column_names.index("rating")
for row in csvreader:
    print(row[_id]+ "\t" + row[rating])
