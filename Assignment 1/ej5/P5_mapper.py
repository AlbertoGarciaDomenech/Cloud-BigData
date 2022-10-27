#!/usr/bin/python

import sys
import csv
# abrimos el archivo csv
csvreader = csv.reader(sys.stdin, delimiter =',')
# en la primera linea conseguimos los nombres de las columnas que queremos acceder
column_names = next(csvreader)
meteorType = column_names.index("recclass")
mass = column_names.index("mass (g)")
for row in csvreader:
    if row[mass] != "":
        print(row[meteorType]+ "\t" + row[mass]) 
    else:
        print(row[meteorType]+ "\t0")
