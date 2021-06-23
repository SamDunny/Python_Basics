import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# get URL from user
url = input('Enter URL - ')

# open given URL, read all contents to the 'html' variable
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# retrieve all the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))