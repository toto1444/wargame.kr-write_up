# -*- coding: utf8 -*-

import urllib, urllib2, time

headers = {'Host': 'wargame.kr:8080'}

data = "?id="
data = data + urllib.quote("adm1ngnngn")
data = data + "&pw="
data = data + urllib.quote("!@SA#$!")
data = data + "&flag="
data = data + urllib.quote("p2F76o5SZlKcPLnvH3aTUIfMr1b0OVzGdkq8QmjBNhJDxAsWeXwY49CyuitRgE")

req = urllib2.Request("http://wargame.kr:8080/adm1nkyj/" + data, '', headers)
response = urllib2.urlopen(req)

res = response.read()
print len(res), res

# id : adm1ngnngn
# Pw : !@SA#$!
# flag : p2F76o5SZlKcPLnvH3aTUIfMr1b0OVzGdkq8QmjBNhJDxAsWeXwY49CyuitRgE
#
# ?id=adm1ngnngn&pw=!@SA#$!&flag=p2F76o5SZlKcPLnvH3aTUIfMr1b0OVzGdkq8QmjBNhJDxAsWeXwY49CyuitRgE