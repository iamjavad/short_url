#!/usr/bin/python3

import pyshorteners
from termcolor import colored

#input!

url = input(str(colored("enter your url:", "blue")))

#short link function
def surl():
	s = pyshorteners.Shortener()
	short = s.tinyurl.short(url)
	print(short)

#check url

if url[0:4] == "http":
	print(colored("True", "green"))
	surl()
else:
	print("url is wrong!")
