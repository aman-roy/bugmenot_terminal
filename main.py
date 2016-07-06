#!/usr/bin/env python
#!path/to/interpretter

# A python program to get bypass registration of many 
# websites with fake logins.

# create by Aman Roy
# Creation Date : 04-JUL-2k16

# Python version used : - Python 2.x

from bs4 import BeautifulSoup
import urllib
import cfscrape
import os

# check for a valid url
def valid(url):
	if "://" in url:
		url = url.split("://")
		url = url[1]
	new = url.split(".")
	if new[-1] > 6 and len(new) > 1:
		return url
	else:
		return None

# Retry again and again for a valid input
def getinput():
	while True:
		mylink = raw_input("Enter website: ")
		mylink = valid(mylink)
		if mylink != None:
			return ("http://bugmenot.com/view/" + mylink)

# pritify the result
def pritify(data):
	data = data.split("Stats:")
	data = data[0]
	data = data.split("Other:")
	final = data[0].split("Password:")
	return (final[0] + "\n" + "Password:" + final[1])

# Get the page content
def content(weblink):
	scraper = cfscrape.create_scraper()
	soup = scraper.get(weblink).content
	fopen = open("VTvedLmrpSMuq329.html", 'w')
	fopen.write(soup)
	fopen.close()

	html_doc = open("VTvedLmrpSMuq329.html")
	soup = BeautifulSoup(html_doc, 'html.parser')
	html_doc.close()
	os.remove("VTvedLmrpSMuq329.html")
	return soup

link = getinput()
html = content(link)

# Get the important part of the file
# and if not get the data print an error.
try:
    nest = html.article.get_text().strip()
except AttributeError:
	print("No data Found..!!")
	quit()

# Pritify the result
print (pritify(nest))