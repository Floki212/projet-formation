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
title = soup.find("article", class_="product_page")
for article in title:
    x = article.find("h1")
    if article.find("h1") and article.find("h1") != -1:
        titles = x
        print(titles)

# Scraper les informations (UPC, prix, stock ...)
info = []
info = soup.findAll("td")
#print(f"INFO {variable} ")

# Scraper la description du livre

description = soup.findAll("article", class_="product_page")
for desc in description:
    description = desc.findAll("p")
#    print(description)

# Scraper la categorie du livre

categorie = soup.findAll("a")

# Scraper l'image du livre

image = soup.findAll("img")

book = {
        "product_page_url": url,
        "product_type": info[1].text,
        "price_excl_tax": info[2].text,
        "price_incl_tax": info[3].text,
        "number_available": info[5].text,
        "number_review": info[6].text,
        "title": titles.text,
        "description": description[3].text,
        "categorie": categorie[3].text,
        "image": image[0],
}
print(book)

#for link in soup.find_all('a'):
    #print(link.get('href'))