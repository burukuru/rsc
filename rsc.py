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
from lxml import etree
from lxml import html
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

def default_opener(cj):
	opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj),urllib.request.HTTPSHandler)
	opener.addheaders = [('User-agent', 'RedditSavedCleaner/0.1a')]
	return opener

def login():
	cj = load_cookie()
	opener = default_opener(cj)
	params = urllib.parse.urlencode({'user': username, 'passwd': password})
	params_bin = params.encode('ascii')
	data = opener.open("https://ssl.reddit.com/post/login", params_bin)
	return cj

def get_saved_links():
	reddit_cookie = login()
	opener = default_opener(reddit_cookie)
	url = "http://reddit.com/user/" + username + "/saved/"
	data = opener.open(url)
	saved = data.read()
	return saved

# Receive div section for an item in etree form and extract info
def extract_info_from_div(saved_item_div):
	sub = saved_item_div.xpath(".//a[contains(@class, 'subreddit')]")
	link = saved_item_div.xpath(".//a[contains(@class, 'title')]")
	print(sub[0].text)
	print(link[0].attrib['href'])
	print(saved_item_div.attrib['data-fullname'])

def delete_item(item_id):
	print(item_id)

def make_download_list():
	saved = get_saved_links()
	tree = html.fromstring(saved)
	#with (open("saved.html")) as savedfile:
	#	tree = html.document_fromstring(savedfile.read())
	pics = tree.xpath("//div[contains(@class, 'saved')]")
	for pic in pics:
		extract_info_from_div(pic)

make_download_list()
