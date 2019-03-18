
import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup

from urllib.request import urlopen

import re

url = urlopen('http://py4e-data.dr-chuck.net/comments_157769.html')

soup = BeautifulSoup(url,"html.parser")

lst = []

sum = 0

for i in soup('span'):
    q = (re.findall(r'\d+',str(i))[0])
    sum += int(q)

print(sum)
