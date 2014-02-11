#!/usr/bin/env python3

# TO DO
'''
login and get links
invalid login
download images
segregate into folders
imgur gallery support

'''

# Import modules
from http import cookiejar
from http import client
import urllib


# Config variables
#
#


def save_cookie():
	# Save cookies to a file for future use
	pass

def load_cookie():
	cj = cookiejar.CookieJar()
	return cj

def login():
# Currently you need to pass a username and password, cookies loaded from browser are in the works
	cj = load_cookie()
	opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj),urllib.request.HTTPSHandler)
	params = urllib.parse.urlencode({'user': 'burukuru', 'passwd': 'password'}) # Replace with prompt
	params_bin = params.encode('ascii')
	data = opener.open("https://ssl.reddit.com/post/login", params_bin)
	return cj

def get_saved_links():
	cj = login()
	opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj),urllib.request.HTTPSHandler)
	data2 = opener.open("https://ssl.reddit.com/user/burukuru/saved/")
	print(data2.read())
	pass

get_saved_links()
