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

# get the url and check for it correctness and 
# if the url is not valid it will quit.
link = raw_input("Enter website: ")
link = valid(link)
if link == None:
	print "Invalid url"
	quit()

link = "http://bugmenot.com/view/" + link

# Bypass cloudflare and save the html to a file
scraper = cfscrape.create_scraper()
soup = scraper.get(link).content
fopen = open("VTvedLmrpSMuq329.html", 'w')
fopen.write(soup)
fopen.close()


# get all the contents of the file to a variable 
# and delete the file
html_doc = open("VTvedLmrpSMuq329.html")
soup = BeautifulSoup(html_doc, 'html.parser')
html_doc.close()
os.remove("VTvedLmrpSMuq329.html")


# Get the important part of the file
# and if not get the data print an error.
try:
    nest = soup.article.get_text().strip()
except AttributeError:
	print("No data Found..!!")
	quit()


# Pritify the result
data = nest.split("Stats:")
data = data[0]
data = data.split("Other:")
final = data[0].split("Password:")
print final[0]
print ("Password:" + final[1])
