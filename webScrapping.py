import urllib
from bs4 import BeautifulSoup

html_doc = urllib.urlopen('http://www.iddbd.net/').read()

soup = BeautifulSoup(html_doc, 'html.parser')

#print soup.prettify()
print soup.a #display anchor tags
print soup.link #show all links