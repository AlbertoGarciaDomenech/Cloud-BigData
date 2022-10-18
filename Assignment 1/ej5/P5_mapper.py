#!/usr/bin/python

import sys
import csv
# abrimos el archivo csv
csvreader = csv.reader(sys.stdin, delimiter =',')
# en la primera linea conseguimos los nombres de las columnas que queremos acceder
column_names = next(csvreader)
_id = column_names.index("id")
name = column_names.index("name")
meteorType = column_names.index("recclass")
mass = column_names.index("mass (g)")
for row in csvreader:
    if row[mass] != "":
        print(row[meteorType]+ "\t" + row[mass]) #+ row[_id] + "\t" + row[name] + "\t" + row[mass])
    else:
        print(row[meteorType]+ "\t0") #+ row[_id] + "\t" + row[name] + "\t" + row[mass])

