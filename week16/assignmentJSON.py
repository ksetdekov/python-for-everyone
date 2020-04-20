import json
import ssl
import urllib.request

# Ignore SSL certificate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = 'http://py4e-data.dr-chuck.net/comments_382344.json'
# address = input('Enter location: ')
# if len(address) < 1:
#     quit()

print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
# print(json.dumps(info, indent=4))
comments = info['comments']
# print(comments)
print('User count:', len(comments))

numbers = list()
for item in comments:
    numbers.append(int(item['count']))

print('Sum:', sum(numbers))
