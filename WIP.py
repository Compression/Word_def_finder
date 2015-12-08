from __future__ import print_function
import requests
import urllib
from bs4 import BeautifulSoup

def get_definition(x):

    url = 'http://services.aonaware.com/DictService/Default.aspx?action=define&dict=wn&query={0}'.format(x)
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    return soup.find('pre', text=True)[0]

lines = []
with open('vocab.txt') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

definitions = []
for line in lines:
    definitions.append(get_definition(line))

out_str = '\n'.join(definitions)
with open('definitions.txt', 'w') as f:
    f.write(out_str)