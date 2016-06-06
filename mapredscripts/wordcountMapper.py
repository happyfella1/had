#!/usr/bin/env python
#!/usr/bin/env python
import sys
import os
def dfmapper():
 for line in sys.stdin:
    word,filename,wordcount = line.strip().split()
    print "%s\t%s\t%d" %(filename,word,int(wordcount))
if __name__ == '__main__':
  dfmapper()