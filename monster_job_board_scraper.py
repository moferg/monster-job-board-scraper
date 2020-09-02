# Marshall Ferguson - Monster Job Board Scraper - 8/2020

# Imports

from urllib.request import urlopen
from bs4 import BeautifulSoup

print('Welcome to the Monster Job Board Scraper!')
print('This script with scrape the Monster website and return job postings.')
job_title_input = input('What job title are you searching for?     ')
location_input = input('What city are you looking to work in?     ')

job_title_url = 'q=' + job_title_input
location_url = '&where=' + location_input

url = 'https://www.monster.com/jobs/search/?' + job_title_url + location_url
# print(url)
page = urlopen(url)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
print(type(soup))