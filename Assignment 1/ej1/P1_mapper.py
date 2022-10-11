#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    words = re.sub(r'\W+', ' ', line).split()
    # ver si la palabra que buscamos esta en esta linea, si si la printeamos (la linea)
    for word in words:
        if(word.lower() == sys.argv[1]):
            print(line)
            