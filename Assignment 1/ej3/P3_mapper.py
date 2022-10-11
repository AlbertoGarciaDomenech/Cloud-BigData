#!/usr/bin/python

import sys
import csv
# abrimos el archivo csv
csvreader = csv.reader(sys.stdin, delimiter =',')
# en la primera linea conseguimos los nombres de las columnas que queremos acceder
column_names = next(csvreader)
date = column_names.index("Date") #la fecha viene en formato yy-mm-dd asi que cogemos el campo antes del primer guion que es el año
value = column_names.index("Close")
for row in csvreader:
    print(row[date].split('-',1)[0] + "\t" + row[value])
