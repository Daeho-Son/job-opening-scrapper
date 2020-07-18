import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

iban_result = requests.get("https://www.iban.com/currency-codes")

iban_soup = BeautifulSoup(iban_result.text, "html.parser")
iban_table = iban_soup.find("table")

country_info = []
for tr in iban_table.find_all("tr")[1:]:
    tds = tr.find_all("td")
    if tds[2].text:
        country_info.append((tds[0].text, tds[2].text))
print(f"len(country_info): {len(country_info)}")
# 길이: 265
country_dictionary = dict(country_info)
print(f"len(country_dictionary): {len(country_dictionary)}")
# 길이: 250
# 아이디어는 좋으나 이렇게 할 경우 중복된 country는 가져오지 못합니다.
# Dictionary의 key는 중복이 되지 않는다.
# 참고: https://wikidocs.net/16 에서 Ctrl+F로 '딕셔너리 만들 때 주의할 사항'검색
country_list = list(country_dictionary.keys())
print(f"len(country_list): {len(country_list)}")
# 길이: 250


for country in country_list:
    index = country_list.index(country)
    numbered_list = f"# {index} {country}"
    print(numbered_list)


def get_amount(first_value2, second_value2):
    while True:
        try:
            num3 = float(input("#: "))
            scrape_result = requests.get(
                f"https://transferwise.com/gb/currency-converter/{first_value2}-to-{second_value2}-rate?amount={num3}"
            )
            scrape_soup = BeautifulSoup(scrape_result.text, "html.parser")
            ratio = scrape_soup.find("input", {"id": "rate"})["value"]
            calculate_result = num3 * float(ratio)
            final_format = format_currency(
                calculate_result, f"{second_value2}", locale="ko_KR"
            )
            print(f"{first_value2} {num3} is {final_format}")
        except:
            print("That wasn't a number")


def get_second_input(first_value):
    while True:
        # while문을 쓰지 않고 재귀함수를 썼으면 좋았을 것이라고 생각됨
        try:
            num2 = int(input("#: "))   
            if int(num2) >= 0 and int(num2) < 265:
                # num2는 이미 위에 int()로 형변환 했기때문에 이렇게 안써도됨.
                # if 0 <= num2 < 265:
                country_identifier2 = country_list[num2]
                second_code = country_dictionary[country_identifier2]
                print(
                    f"How many {first_value} do you want to convert to {second_code}?"
                )
                get_amount(first_value, second_code)
            else:
                print("Choose a number from the list")
        except:
            print("That wasn't a number")


def get_input():
    print("Where are you from? Choose a country by name.")
    while True:
        try:
            num = int(input("#: "))
            if int(num) >= 0 and int(num) < 265:
                country_identifier = country_list[num]
                print("You choose\n", country_identifier)
                first_code = country_dictionary[country_identifier]
                print("\nNow choose another country./n")
                get_second_input(first_code)
            else:
                print("Choose a number from the list")
        except:
            print("That wasn't a number")


get_input()

