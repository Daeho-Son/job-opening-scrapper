import requests
from bs4 import BeautifulSoup


url = "https://www.iban.com/currency-codes"
soup = BeautifulSoup(requests.get(url).text, "html.parser")


def get_data():
    currency_dic_list = []
    for tr in soup.select("tbody > tr"):
        td = tr.find_all("td")
        name = td[0].text.capitalize()
        code = td[2].text
        if name and code:
            currency_dic_list.append({"country": name, "code": code})

    return currency_dic_list