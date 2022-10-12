#!/usr/bin/python

import sys
import re
import math

for line in sys.stdin:
    movieId,rating = line.split("\t",1)
    if(float(rating) == 0.0):
        print("1\t" + movieId)
    else:
        print(str(math.ceil(float(rating))) + "\t" + movieId)
