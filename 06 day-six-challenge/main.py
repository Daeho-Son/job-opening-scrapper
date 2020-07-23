import os
from babel.numbers import format_currency
from get_datas import get_currency_codes, get_exchage
from check import check_number


os.system("clear")


data = get_currency_codes()
print("Hello! Please choose select a country by number:")
for count, data_i in enumerate(data):
    print(f"# {count} {data_i.get('country')}")


# from_country
print("\nWhere are you from? Choose a country by number.\n")
from_country = data[check_number(len(data))]
print(f"{from_country.get('country')}\n")


# to_country
print("Now choose another country.\n")
to_country = data[check_number(len(data))]
print(f"{from_country.get('country')}\n")


# exchange
from_code = from_country.get("code")
to_code = to_country.get("code")
amount = check_number("", from_code, to_code)
print(f'{format_currency(amount, from_code, locale="ko_KR")} is ', end="")
print(
    f'{format_currency(get_exchage(from_code, to_code, amount), to_code, locale="ko_KR")}'
)
