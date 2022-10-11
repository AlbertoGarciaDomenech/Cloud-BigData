#!/usr/bin/python

import sys

previous = None
sum = 0 #veces que aparece una pelicula
agg_val = 0 #sumatorio de el valor de todas las ratings de una pelicula

for line in sys.stdin:
    key, value = line.split('\t')

    if key != previous:
        if previous is not None:
            print(previous + '\t' + str(float(agg_val)/sum))
        previous = key
        sum = 0
        agg_val = 0
    
    sum += 1
    agg_val += float(value)

print(key + '\t' + str( float(agg_val)/sum))
