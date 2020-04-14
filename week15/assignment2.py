import ssl
import urllib.request

from bs4 import BeautifulSoup

# ignore ssl certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
count = int(input('Enter count:'))
pos = int(input('Enter position:'))

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#  get anchor tags
tags = soup('a')
# for tag in tags:
# print(tag.get('href', None))
result = tags[pos - 1].get('href', None)
print(url)
print(result)
