import requests
from BeautifulSoup import BeautifulSoup

word = raw_input('Paste your word ')

url = 'https://www.google.com/?gws_rd=ssl#safe=off&q=%s' % word

print url
response = requests.get(url)
html = response.content
print html

soup = BeautifulSoup(html)
print soup.prettify()