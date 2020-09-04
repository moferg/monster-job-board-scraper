# Marshall Ferguson - Monster Job Board Scraper - 8/2020

# Imports

from urllib.request import urlopen
from bs4 import BeautifulSoup
import mechanicalsoup
from mechanicalsoup.utils import LinkNotFoundError

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
links_all = browser.links()
# print(links_all)

link_text = []
for link in links_all:
    link_text.append(link.get_text())
# print(link_text)

job_titles = []
for job_title in job_titles_text:
    job_titles.append(job_title.strip('\r\n'))
links = []
for link in link_text:
    links.append(link.strip('\r\n'))
# print(job_titles)
# print(links)

job_links_text = []
for link in links:
    for job_title in job_titles:
        if link == job_title:
            job_links_text.append(link)
# print(job_links_text)

job_links = []
for link in links_all:
    for job_link in job_links_text:
        if link.get_text().strip('\r\n') == job_link:
            job_links.append(link)
            # print(job_links)
# print(job_links)

job_link_hrefs = []
for link in job_links:
    job_link_hrefs.append(link.get('href'))
    job_link_hrefs = list(dict.fromkeys(job_link_hrefs))
# print(job_link_hrefs)

job_descriptions = []
for href in job_link_hrefs:
    try:
        browser.open(href)
        job_description = browser.get_current_page().find('div', class_ = 'job-description')
        job_descriptions.append(job_description.get_text())
    except LinkNotFoundError:
        print('There was a LinkNotFoundError')
 
print(job_descriptions)