import re

text = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'
y = re.findall('href="(.+)"', text)
print(y)
