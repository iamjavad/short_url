#!/usr/bin/python3

import pyshorteners

#input!

url = input(str("enter your url:"))

#short link function
def surl():
	s = pyshorteners.Shortener()
	short = s.tinyurl.short(url)
	print(short)

#check url

if url[0:4] == "http":
	print("True")
	surl()
else:
	print("url is wrong!")
