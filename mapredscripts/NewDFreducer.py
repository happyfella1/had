#!/usr/bin/env python
import sys
import math
def dfreducer():
  curword = None
  curcount = None
  space = []
  for line in sys.stdin:
    word, filename, wordcount, totalwords, count = line.strip().split()
    prefix = "%s\t%s\t%s" %(word,filename,wordcount)
    if word == None:
      curword = word
      curcount = eval(count)
      space.append(prefix)
    elif curword == word:
      curcount += eval(count)
      space.append(prefix)
    else:
      for item in space:
        print "%s\t%d\t%s" % (item,curcount,(math.log(2/curcount) * eval(item.split("\t")[2])/2))
      curword = word
      curcount = eval(count)
      space = [prefix]
  for item in space:
    print "%s\t%d\t%d" % (item,curcount,(math.log(2/curcount) * eval(item.split("\t")[2])/2))
if __name__=='__main__':
  dfreducer()
