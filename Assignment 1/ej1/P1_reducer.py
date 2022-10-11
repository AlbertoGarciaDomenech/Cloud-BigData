#!/usr/bin/python

import sys

previous = None

for line in sys.stdin:
    if line != previous:
        if previous is not None:
            print(previous)
        previous = line
    

print(previous)