import requests
from bs4 import BeautifulSoup
import csv
import urllib3

    #Every page and books link to scrape
url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
response = requests.get(url)
#soup = BeautifulSoup(url)
soup = BeautifulSoup(response.content, "html.parser")
links = soup.find_all("td")
#for link in soup.find_all("a"):
print(links)   

