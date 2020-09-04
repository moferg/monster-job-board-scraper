# Marshall Ferguson - Monster Job Board Scraper - 8/2020

# Imports

from urllib.request import urlopen
from bs4 import BeautifulSoup
import mechanicalsoup

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
# print(type(soup))

job_titles_html = soup.find_all('h2', class_ = 'title')
# print(job_titles_html)
job_titles_text = []
for job_title in job_titles_html:
    job_titles_text.append(job_title.get_text())
# print(job_titles_text)

browser = mechanicalsoup.StatefulBrowser()
browser.open(url)
links = browser.links()

link_text = []
# print(links)
for link in links:
    link_text.append(link.get_text())
# print(link_text)

job_titles = []
for job_title in job_titles_text:
    job_titles.append(job_title.strip('\r\n'))
links = []
for link in link_text:
    links.append(link.strip('\r\n'))
print(job_titles)
print(links)