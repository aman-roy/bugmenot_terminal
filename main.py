from bs4 import BeautifulSoup
import urllib
import cfscrape
import os

link = raw_input("Enter website: ")
link = "http://bugmenot.com/view/" + link

scraper = cfscrape.create_scraper()
soup = scraper.get(link).content
fopen = open("VTvedLmrpSMuq329.html", 'w')

fopen.write(soup)
fopen.close()

html_doc = open("VTvedLmrpSMuq329.html")
soup = BeautifulSoup(html_doc, 'html.parser')
html_doc.close()
os.remove("VTvedLmrpSMuq329.html")

try:
    nest = soup.article.get_text().strip()
except AttributeError:
	print("No data Found..!!")
	quit()

data = nest.split("Stats:")
data = data[0]
data = data.split("Other:")
final = data[0].split("Password:")
print final[0]
print ("Password:" + final[1])