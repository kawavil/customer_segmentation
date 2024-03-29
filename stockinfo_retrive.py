from typing import Dict

from bs4 import BeautifulSoup
import requests


def get_price(url):
    url_contents = requests.get(url)
    soup = BeautifulSoup(url_contents.content, "html.parser")
    div = soup.find("div", {"class": "YMlKec fxKbKc"})
    price = div.text
    return price


def get_quotes():
    stocks_dict = {"NIFTY 50": "https://www.google.com/finance/quote/NIFTY_50:INDEXNSE",
                   "SENSEX": "https://www.google.com/finance/quote/SENSEX:INDEXBOM",
                   "NIFTY BANK": "https://www.google.com/finance/quote/NIFTY_BANK:INDEXNSE",
                   "NIFTY MIDCAP 50": "https://www.google.com/finance/quote/NIFTY_MIDCAP_50:INDEXNSE"
                   # 'tcs': "https://www.google.com/finance/quote/TCS:NSE",
                   # 'hul': 'https://www.google.com/finance/quote/HINDUNILVR:NSE',
                   # "reliance": "https://www.google.com/finance/quote/RELIANCE:NSE",
                   # 'kotakbank': "https://www.google.com/finance/quote/KOTAKBANK:NSE"
                   }
    pricedict = {}
    for index, url in stocks_dict.items():
        price = get_price(url)
        pricedict[index] = price
        print(index)

    print("Now you can run the server")
    return pricedict
