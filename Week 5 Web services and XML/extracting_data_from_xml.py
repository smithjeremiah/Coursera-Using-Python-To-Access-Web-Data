import xml.etree.ElementTree as ET

import urllib.request

url = input('Enter location:') #http://py4e-data.dr-chuck.net/comments_42.xml
print('Retreiving' + url)

xml = urllib.request.urlopen(url)
xml = xml.read()
tree = ET.fromstring(xml)

print('Retreived ' + len(xml) + ' characters')

stuff = tree.findall('.//count')

sum = 0

for i in stuff:
    sum += int(i.text)

print('Count:' + len(stuff))
print('Sum:' + sum)
