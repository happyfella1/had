import urllib2
import numpy
import random
from time import sleep
from bs4 import BeautifulSoup
pages =numpy.arange(0, 1000, 50)
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

# run this script with all they keywords that needed to crawl
for pageno in pages:
    my_url = 'http://www.indeed.com/resumes?q=fashion&l=Philadelphia%2C+PA&co=US&start='+str(pageno)
    req = urllib2.Request(my_url,headers=hdr)
    sleep(10)
    html=urllib2.urlopen(req).read()
    soup = BeautifulSoup(html)
    current_link = ''
    current_link_inner = ''
    for link in soup.find_all('a', href=True):
        current_link = link.get('href')
        try:
            if current_link.endswith('sp=0'):
                turl='http://www.indeed.com'+current_link
                turl=turl.strip('?sp=0')
                print turl+'/pdf'

        except urllib2.HTTPError, e:
            print str(e.code)+e.msg


