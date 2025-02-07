
import requests
from bs4 import BeautifulSoup

def scrape_gold_price():
    url = "https://www.example.com/gold-prices"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    price = soup.find("div", class_="price").text
    return price