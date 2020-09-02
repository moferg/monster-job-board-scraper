# Marshall Ferguson - Monster Job Board Scraper - 8/2020

# Imports

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.monster.com/'
page = urlopen(url)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

print(soup)