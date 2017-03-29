import os.path
from multiprocessing import Pool
import sys
import time
import glob
from collections import deque
from filelock import FileLock
import filelock
import fcntl



questions=deque()

def process_file(name):
    linecount=0
    wordcount={}
    with open(name, 'r') as inp:
        for line in inp:
            line = line.strip()
            words = line.split()
            for word in words:
                word = word.replace("'","").replace("!","").replace(".","").replace(",","").replace("-","").replace(";","").replace("?","").replace("/","").replace("*","").replace("[","").replace("]","").replace(":","")
            if word not in wordcount:
                     wordcount[word] = 1
            else:
                     wordcount[word] += 1

    for k,v in wordcount.items():
        questions.append([k,v])
        f = open('myfile.txt','a')
        x = open('foo', 'w+')
        fcntl.flock(f, fcntl.LOCK_EX)
        str = k + " " + `v` + "\n"
        f.write(str)
        fcntl.flock(f, fcntl.LOCK_UN)
        f.close()


    return questions

def f(arg, dirname, names):
    pool=Pool()
    list = []
    pool.map(process_file, [os.path.join(dirname, name) for name in names])
    dict = {}






if __name__ == '__main__':
    start=time.time()
    os.path.walk('input/', f, None)

    file = open('myfile.txt')
    sys.stdin = file

    words = {}

    for x in sys.stdin:
        linearr = x.split(" ")
        if linearr[0] not in words:
            words[linearr[0]] = int(linearr[1])
        else:
            words[linearr[0]] += int(linearr[1])

    for k,v in words.items():
        print k ,v



