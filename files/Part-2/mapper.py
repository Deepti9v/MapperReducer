#!/usr/bin/env python

import sys, urllib, re
import os

counter = [0] *26;

count = 0
wordcount={}
for line in sys.stdin:
   line = line.strip()
   words = line.split()
   for word in words:
        word = word.replace("'","\n")
        if word in ("chastity","languish","death"):
            if word not in wordcount:
                 wordcount[word] = 1
            else:
                 wordcount[word] += 1
head , fname = os.path.split(os.environ['map_input_file'])
#print fname, count
#print fname,len(wordcount)
for k,v in wordcount.items():
 print fname,k,v
