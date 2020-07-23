import requests
from bs4 import BeautifulSoup


url = "https://www.iban.com/currency-codes"
soup = BeautifulSoup(requests.get(url).text, "html.parser")


# 수정 후
def get_data():
    print(url)
    currency_dic_list = []
    for tr in soup.select("tbody > tr"):
        td = tr.find_all("td")
        name = td[0].text
        code = td[2].text
        if name and code:
            currency_dic_list.append({"country": name, "code": code})

    return currency_dic_list


# 수정 전
# def get_data():
#     td_tag = []
#     for i in soup.select("tbody > tr"):
#         td_tag.append(i.find_all("td"))

#     currency_dic = []
#     for i in td_tag:
#         if i[1].string == "No universal currency":
#             pass
#         else:
#             currency_dic.append(
#                 {"country": i[0].string.capitalize(), "code": i[2].string}
#             )
#     return currency_dic
