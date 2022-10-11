#!/usr/bin/python

import sys

range = {}

for line in sys.stdin:
        
    key, value = line.split('\t')
    if key in range.keys():
            range[key].append(value.split("\n",1)[0])
    else:
        range[key] = [value.split("\n",1)[0]]

for i in range.keys():
    print("Rango " + (i) + ": ")
    print(str(range.get(i)))
