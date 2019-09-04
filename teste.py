import requests
from bs4 import BeautifulSoup

with open('arquivo.html', 'r') as f:
	soup_string = BeautifulSoup(f.read(), 'html.parser')
print(soup_string)

r = requests.get('http://www.google.com')
soup = BeautifulSoup(r.text, 'lxml')
print(soup)

with open('arquivo.html', 'r') as f:
	soup_string = BeautifulSoup(f.read(), 'html5lib')
print(soup_string)