# Marshall Ferguson - Monster Job Board Scraper - 8/2020

# Imports

from urllib.request import urlopen
from bs4 import BeautifulSoup

# print('Welcome to the Monster Job Board Scraper!')
# print('This script with scrape the Monster website and return job postings.')
# job_title_input = input('What job title are you searching for?     ')
# location_input = input('What city are you looking to work in?     ')

# job_title_url = 'q=' + job_title_input
# location_url = '&where=' + location_input

# url = 'https://www.monster.com/jobs/search/?' + job_title_url + location_url
# print(url)
url = 'https://www.monster.com/jobs/search/?q=software-developer&where=louisville'     # This url is for testing purposes
page = urlopen(url)
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
job_titles_html = soup.select('.card-header a')
# print(job_titles_list)
for job_titles in job_titles_html:
    job_title = job_titles.get_text()
    print(job_title)