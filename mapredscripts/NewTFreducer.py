import sys

#reducer to count number of times a word appeared in a document
def tfreducer():
  curprefix = None
  curcount = None
  mycount=0
  for data in sys.stdin:
     word,filename,count = data.strip().split('\t')
     prefix = '%s\t%s' % (word,filename)
     if curprefix == None:
      curprefix = prefix
      curcount = eval(count)
     elif curprefix == prefix:
      curcount += eval(count)
     else:
      mycount+=curcount
      print "%s\t%s" % (curprefix,curcount)
      curprefix = prefix
      curcount = eval(count)
  # mycount+=curcount
  print "%s\t%s" % (curprefix,curcount)

if __name__ == '__main__':
  tfreducer()