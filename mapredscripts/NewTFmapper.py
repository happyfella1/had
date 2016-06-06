 #!/usr/bin/env python
#Mapper to count number of times a word appeared in the document
import sys
import os

def tfmapper():

  for line in sys.stdin:
    words = line.strip().lower().split()
    # i=0;
    # myfile=None
    for word in words:
      print "%s\t%s\t1" % (word,"file1")
if __name__ == '__main__':
  tfmapper()