#!/usr/bin/env python

import sys, urllib, re
import glob

words = {}

arguments  = glob.glob('*.txt')  

for argument in arguments:
    file = open(argument)
    sys.stdin = file
    for x in sys.stdin:
        linearr = x.split(" ")
        if linearr[0] not in words:
            words[linearr[0]] = int(linearr[1])
        else:
            words[linearr[0]] += int(linearr[1])

for k,v in words.items():
        print k ,v







