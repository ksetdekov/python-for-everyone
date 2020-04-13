import urllib.request
from bs4 import BeautifulSoup

url = input('Enter url')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#  get anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
    print(tag)
