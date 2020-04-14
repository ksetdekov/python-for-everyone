import ssl
import urllib.request

from bs4 import BeautifulSoup

# ignore ssl certificate error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Amnah.html'
count = int(input('Enter count:'))
pos = int(input('Enter position:'))
print(url)


def fall(link, n):
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html, 'html.parser')
    #  get anchor tags
    tags = soup('a')
    # for tag in tags:
    # print(tag.get('href', None))
    result = tags[n - 1].get('href', None)
    print(result)
    return result


while count > 0:
    url = fall(url, pos)
    count += -1
