import urllib2
import urllib
import requests
import wget
import sys
import time

textFile = sys.argv[1].strip()
urls = open(textFile).read().splitlines()

print len(urls)
for url in urls:
    print url
    try:
        wget.download(url)
	sleep(1)
    except:
        continue




# r = requests.get("http://www.indeed.com/r/Neha-Suresh/680aea9b3cd4acb6/pdf")
# r = wget.download("http://www.indeed.com/r/Neha-Suresh/680aea9b3cd4acb6/pdf")
# print r
# open("Neha-Suresh" , 'wb').write(r.content)

