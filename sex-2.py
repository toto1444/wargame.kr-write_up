# -*- coding: utf8 -*-

import urllib, urllib2, time, random


a = "착한생각착한생각학한섹각착한생각착한섹스각착한생각"
sex = ''.join(random.sample(a,len(a)))
ass = "착한생각착한생각학한섹각착한생각착한섹스각착한생각"

count = 2
c = 0

#print("횟수 : ")
#input(int(count))


while(1):
    for i in range(0,len(ass)):
        print a
        c = c + 1
    if count >= c:
        print "\nfailed"
        print "origin:" + a
        break
    else:
        print c