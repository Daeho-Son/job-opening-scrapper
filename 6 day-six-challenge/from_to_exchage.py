import requests
from bs4 import BeautifulSoup


def exchage(from_code, to_code, amount):
    url = f"https://transferwise.com/gb/currency-converter/{from_code}-to-{to_code}-rate?amount={amount}"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    rate = float(
        soup.select(
            "div.js-Calculator > form > div.m-t-3 > div.col-lg-6 > h3.cc__source-to-target > span.text-success"
        )[0].text
    )
    return rate * amount
