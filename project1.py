import requests
from bs4 import BeautifulSoup
import csv

#premier livre a scrape
url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
#if response.status_code -- 200:
#else:
#    print("erreur de connexion")

# Link du livre

#links = []
#link = soup.find("article")
#for a in soup.find("a", href=True):
#    links.append(a["href"])

# Scraper le titre du livre
titles = []
title = soup.find("article", class_="product_page")
for article in title:
    titles = article.find("h1")
    print(titles)

# Scraper les informations (UPC, prix, stock ...)
info = []
info = soup.findAll("td")
print(info)

# Scraper la description du livre

descriptions = []
description = soup.find("article", class_="product_page")
for desc in description:
    description = desc.find("p", h2=True)
    print(description)

#if response.status_code -- 200:
#    else:
#        print("erreur de connexion")

book = {
        "product_type": info[1],
        "price_excl_tax": info[2],
        "price_incl_tax": info[3],
        "number_available": info[5],
        "number_review": info[6],
}
print(book)
