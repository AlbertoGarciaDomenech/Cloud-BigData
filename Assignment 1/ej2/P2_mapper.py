#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    words = line.split("\"")[1]
    if ("GET" in words) or ("POST" in words) or ("HEAD" in words):
        print(words.split(" ")[1] + "\t1")