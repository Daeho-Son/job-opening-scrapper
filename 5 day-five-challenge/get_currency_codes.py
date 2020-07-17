import requests
from bs4 import BeautifulSoup


url = "https://www.iban.com/currency-codes"
soup = BeautifulSoup(requests.get(url).text, "html.parser")


def get_data():
    td_tag = []
    for i in soup.select("tbody > tr"):
        td_tag.append(i.find_all("td"))

    currency_dic = []
    for i in td_tag:
        if i[1].string == "No universal currency":
            pass
        else:
            currency_dic.append(
                {"country": i[0].string.capitalize(), "code": i[2].string}
            )
    return currency_dic
