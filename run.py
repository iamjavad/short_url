#!/usr/bin/python3

import pyshorteners

url = input(str("enter your url:"))
s = pyshorteners.Shortener()
short = s.tinyurl.short(url)
print(short)
