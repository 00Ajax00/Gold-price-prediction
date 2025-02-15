import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

URL = "https://www.goldprice.org/"

def scrape_gold_price():
    try:
        response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)

        soup = BeautifulSoup(response.text, "html.parser")

        # Example: Adjust selector based on the actual site structure
        price_element = soup.select_one(".gold-price, .some-other-class")
        if not price_element:
            raise ValueError("Gold price element not found.")

        price = price_element.text.strip()
        return {"gold_price": price}
    
    except requests.RequestException as e:
        logger.error(f"Request failed: {e}")
        return None
    except Exception as e:
        logger.error(f"Scraping error: {e}")
        return None

if __name__ == "__main__":
    gold_data = scrape_gold_price()
    if gold_data:
        df = pd.DataFrame([gold_data])
        df.to_csv("gold_prices.csv", index=False)
        logger.info("Gold prices saved to CSV.")
