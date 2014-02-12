#!/usr/bin/env python3

# TO DO
'''
invalid login
download images
segregate into folders
imgur gallery support

'''

# Import modules
from http import cookiejar
import urllib
import getpass

# Load credentials from file
def get_userpass():
	file = open("rsc.cfg", "r")
	creds = file.readlines()
	for i,j in enumerate(creds):
		    creds[i] = j.rstrip()
	return creds

# Config variables
creds = get_userpass()
username = creds[0]
password = creds[1]

def load_cookie():
	cj = cookiejar.CookieJar()
	return cj

def login():
	cj = load_cookie()
	opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj),urllib.request.HTTPSHandler)
	params = urllib.parse.urlencode({'user': username, 'passwd': password})
	params_bin = params.encode('ascii')
	data = opener.open("https://ssl.reddit.com/post/login", params_bin)
	return cj

def get_saved_links():
	cj = login()
	opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj),urllib.request.HTTPSHandler)
	url = "https://ssl.reddit.com/user/" + username + "/saved/"
	data2 = opener.open(url)
	print(data2.read())
	pass

get_saved_links()
