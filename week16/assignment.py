import ssl
import urllib.request
import xml.etree.ElementTree as ElemTree

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# address ='http://py4e-data.dr-chuck.net/comments_42.xml'
address = input('Enter location: ')
if len(address) < 1:
    quit()

print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
# print(data.decode())
tree = ElemTree.fromstring(data)

counts = tree.findall('.//count')
print('count:', len(counts))
# print(counts)
numbers = list()
for item in counts:
    numbers.append(int(item.text))

print('Sum:', sum(numbers))
