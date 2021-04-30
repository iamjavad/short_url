#!/usr/bin/python3

import pyshorteners

url = input(str("enter your url:"))
def surl():
	s = pyshorteners.Shortener()
	short = s.tinyurl.short(url)
	print(short)

def check():
	if url[0:4] == "http":
		print("True")
		surl()
	else:
		print("url is wrong!")
check()
