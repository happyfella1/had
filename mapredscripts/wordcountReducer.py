#!/usr/bin/env python

from operator import itemgetter
import sys
import string
current_word = None
total_count = 0
word = None
myfile=None
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    filename, word, count = line.split('\t')

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:

        continue
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if myfile == filename:
        if total_count>0:
         total_count += count
         filename +=str(total_count)
         print '%s\t%s\t%d' % (filename,word, count)
    else:
        if filename:
            # write result to STDOUT
            new =filename+str(",0")
            print '%s\t%s\t%d' % (filename,word, count)
        total_count = count
        myfile = filename
