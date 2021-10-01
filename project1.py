import requests
from bs4 import BeautifulSoup
import csv
import urllib3

#premier livre a scrape
url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Link du livre

links = []
link = soup.find("article")
for a in soup.find("a", href=True):
    links.append(a["href"])

# Scraper le titre du livre
titles = []
title = soup.find("article")
for article in title:
    titles = article.find("h1")
    print(titles)

# Scraper les informations (UPC, prix, stock ...)

upc = soup.find("td")
print(upc)

product = soup.find("td")
print(product)

