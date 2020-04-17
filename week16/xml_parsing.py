# xml parsing

import xml.etree.ElementTree as ElemT  # this is an alias

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''  # multiline string

tree = ElemT.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

input_data = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ElemT.fromstring(input_data)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name2', item.find('name').text)
    print('Id2', item.find('id').text)
    print('Attribute2', item.get('x'))
