#!/usr/bin/python

import sys
import re
import math

for line in sys.stdin:
    words = re.sub(r'\W+', ' ', line).split()
    
    if(float(words[1]) == 0):
        print("1\t" + words[0])
    else:
        print(str(math.ceil(float(words[1]))) + "\t" + words[0])
