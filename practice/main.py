import os
import requests
from bs4 import BeautifulSoup as bs

os.system("clear")
url = "https://www.iban.com/currency-codes"

indeed_result = requests.get(url)
indeed_soup = bs(indeed_result.text, "html.parser")
test = indeed_soup.select("table > tbody td")


def select_country(arr):
    try:
        num = int(input("#: "))
        if num in arr:
            print("You chose " + arr[num][0] + "\nThe currency code is " + arr[num][1])
        else:
            print("Choose a number from the list.")
            return select_country(arr)
    except:
        print("That wasn't a number.")
        return select_country(arr)


def iban():
    countries_and_alphaCode = {}
    count = 0
    for i in range(len(test)):
        if i % 4 == 1 and test[i].text != "No universal currency":
            # Save Country, Alpha_3_Code in dictionary.
            countries_and_alphaCode[count] = (
                test[i - 1].text.capitalize(),
                test[i + 1].text,
            )
            count += 1  # Add count if key, value added.
    print("Hello! Please choose select a country by number:")
    for i in range(count):
        print("# " + str(i) + " " + countries_and_alphaCode[i][0])
    select_country(countries_and_alphaCode)


iban()
