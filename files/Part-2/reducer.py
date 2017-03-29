#!/usr/bin/env python
from operator import itemgetter
import sys
import os

counter = [0] * 26;
file_name = {}

file_flag_c = {}
file_flag_d = {}
file_flag_l = {}

linearr = {}

l1 = []
l2 = []
l3 = []
str1 = ""
str2 = ""
str3 = ""

for x in sys.stdin:

    linearr = x.split(" ")
    if ( file_flag_l.has_key(linearr[0]) == False ):
       file_flag_l[linearr[0]] = False
       file_name[linearr[0]] = 0
    if   ( file_flag_c.has_key(linearr[0]) == False ):
       file_flag_c[linearr[0]] = False
       file_name[linearr[0]] = 0
    if   ( file_flag_d.has_key(linearr[0]) == False ):
       file_flag_d[linearr[0]] = False
       file_name[linearr[0]] = 0

    if ( linearr[1] == "chastity" and file_flag_c[linearr[0]] <> True ) :
      file_name[linearr[0]] += 1
      file_flag_c[linearr[0]] = True
    elif ( linearr[1] == "languish" and file_flag_l[linearr[0]] <> True):
      file_name[linearr[0]] += 1
      file_flag_l[linearr[0]] = True
    elif linearr[1] == "death" and file_flag_d[linearr[0]] <> True:
      file_name[linearr[0]] += 1
      file_flag_d[linearr[0]] = True


for k,v in file_name.items():
 #print k,v
  if v == 1:
     l1.append(k)
  elif v == 2:
     l2.append(k)
  elif v == 3:
     l3.append(k)

for p in l1:
    str1 = str1 + " " + p
for p in l2:
    str2 = str2 + " " + p
for p in l3:
    str3 = str3 + " " + p

print str1 + " are the files containing only one word"
print str2 + " are the files containing only two words"
print str3 + " are the files containing all three words"
