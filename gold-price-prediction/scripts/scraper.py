import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.goldprice.org/"

def scrape_gold_price():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    # Example: Modify this based on actual site structure
    price = soup.find("div", {"class": "gold-price"}).text.strip()
    
    return {"gold_price": price}

if __name__ == "__main__":
    gold_data = scrape_gold_price()
    df = pd.DataFrame([gold_data])
    df.to_csv("gold_prices.csv", index=False)
