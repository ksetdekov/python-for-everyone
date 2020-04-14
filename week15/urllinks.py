import ssl
import urllib.request

from bs4 import BeautifulSoup

# ignore ssl certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#  get anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
