import requests
from bs4 import BeautifulSoup


# country와 code를 가져오는 함수.
def get_currency_codes():
    url = "https://www.iban.com/currency-codes"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    currency_dic_list = []
    for tr in soup.select("tbody > tr"):
        td = tr.find_all("td")
        name = td[0].text.capitalize()
        code = td[2].text
        if name and code:
            currency_dic_list.append({"country": name, "code": code})
    return currency_dic_list


# 환율을 가져오는 함수.
def get_exchage(from_code, to_code, amount):
    url = f"https://transferwise.com/gb/currency-converter/{from_code}-to-{to_code}-rate?amount={amount}"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    rate = float(soup.select("div.js-Calculator > form > input")[0]["value"])
    return rate * amount
