import os
import requests
from bs4 import BeautifulSoup as bs
from babel.numbers import format_currency

os.system("clear")
url = "https://www.iban.com/currency-codes"

def crawl():
    crawl_result = requests.get(url)
    crawl_soup = bs(crawl_result.text, "html.parser")
    test = crawl_soup.select(
        "body > div.boxed > div.flat-row.pad-top20px.pad-bottom70px > div > div > div > div > table > tbody td"
    )
    countries_and_alphaCode = {}
    count = 0
    for i in range(len(test)):
        if i % 4 == 1 and test[i].text != "No universal currency":
            # Save Country, Alpha_3_Code in dictionary. ex) { 126 : Korea (the republic of), KRW }
            countries_and_alphaCode[count] = test[i - 1].text.capitalize(), test[i + 1].text
            count += 1  # Add count if key, value added.
    return countries_and_alphaCode

def select_country_A(arr):
    try:
        num = int(input("\nWhere ar you from? Choose a country by number.\n#: "))
        if num in arr:
            print(arr[num][0])
            return arr[num][1]
        else:
            print("Choose a number from the list.")
            return select_country_A(arr)
    except:
        print("That wasn't a number.")
        return select_country_A(arr)

def select_country_B(arr):
    try:
        num = int(input("\nNow choose another country.\n#: "))
        if num in arr:
            print(arr[num][0])           
            return arr[num][1]
        else:
            print("Choose a number from the list.")
            return select_country_B(arr)
    except:
        print("That wasn't a number.")
        return select_country_B(arr)

def convert(country_A, country_B):
    try:
        convert_amount = float(
            input("\nHow Many " + country_A + " do you want to convert to "+country_B+"?\n"))
        convert_url = "https://transferwise.com/gb/currency-converter/" + country_A + "-to-" + country_B +"-rate?amount=" + str(convert_amount)
        convert_result = requests.get(convert_url)
        convert_soup = bs(convert_result.text, "html.parser")
        convert_success = float(convert_soup.find("span", {"class": "text-success"}).text)*convert_amount
        print(format_currency(convert_amount, country_A, locale="ko_KR") ,"is", format_currency(convert_success, country_B, locale="ko_KR"))
    except:
        print("That wasn't a number.")
        convert(country_A, country_B)
    
def main():
    data = crawl()
    print("Welcome to CurrecyConvert PRO 2000\n")
    for idx,i in enumerate(data):
        print(f"#{idx} {data[i][0]}")
    convert(select_country_A(data),select_country_B(data))

main()