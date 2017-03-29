from threading import Thread
import time
import Queue
import sys, urllib, re
import glob
import time
import ast


def read_file(arg, queue):
    result = (arg)
    dict = {}
    file = open(arg)
    sys.stdin = file
    wordcount = {}
    for line in sys.stdin:
        line = line.strip()
        words = line.split()
        for word in words:
            word = word.replace("'","").replace("!","").replace(".","").replace(",","").replace("-","").replace(";","").replace("?","").replace("/","").replace("*","").replace("[","").replace("]","").replace(":","")

            if word not in wordcount:
                     wordcount[word] = 1
            else:
                     wordcount[word] += 1
    queue.put({arg: wordcount})
    #if queue is full, then call a function

def combine():
    arguments  = glob.glob('*.txt')  #get all the text files
    q = Queue.Queue()
    threads = []
    for argument in arguments:
        #print argument
        t = Thread(target=read_file,args=(argument, q))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    my_dict = {}
    while not q.empty():
     val = q.get()
     # getting the values and im appending it all to dictionary
     for k,v in val.items():
        my_dict[k] = v

    return my_dict

my_dict_final = combine()
word_count1 = {}

for k,v in my_dict_final.items():
   for k1,v1 in v.items():
    #print k1,v1
    if k1 not in word_count1:
        word_count1[k1] = 1
    else:
        word_count1[k1] += 1

word_count1.pop("", None)

for k1,v1 in word_count1.items():
      print k1,v1

