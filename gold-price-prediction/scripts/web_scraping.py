import requests
from bs4 import BeautifulSoup

def fetch_gold_price():
    url = "https://www.example.com/gold-prices"  # Replace with actual source
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    price = soup.find("span", {"class": "gold-price"}).text
    return float(price.replace(",", ""))

print(fetch_gold_price())
