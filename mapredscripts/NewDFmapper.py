#!/usr/bin/env python
import sys
import os
def dfmapper():
    for data in sys.stdin:
        filename, word, wordcount = data.strip().split()
        print"%s\t%s\t%s\t%s" %(word, filename, wordcount)

if __name__ == '__main__':
  dfmapper()