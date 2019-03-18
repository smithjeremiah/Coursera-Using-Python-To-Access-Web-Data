import json

import urllib.request

fh = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.json')

data = json.loads(fh.read())

sum = 0

for i in data['comments']:
    sum += i['count']
print(sum)
