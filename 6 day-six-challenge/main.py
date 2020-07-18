import os
from babel.numbers import format_currency
from get_currency_codes import get_data as currency_codes
from check_number import check
from from_to_exchage import exchage


os.system("clear")

# print(format_currency(5000, "KRW", locale="ko_KR"))

data = currency_codes()
print("Hello! Please choose select a country by number:")
for count, data_i in enumerate(data):
    print(f"# {count} {data_i.get('country')}")


# from
print("\nWhere are you from? Choose a country by number.\n")
from_country = data[check(len(data))]
print(f"{from_country.get('country')}\n")

# to
print("Now choose another country.\n")
to_country = data[check(len(data))]

# exchange
from_code = from_country.get("code")
to_code = to_country.get("code")
print(f"How many {from_code} do you want to convert to {to_code}?")
amount = check()
print(f'{format_currency(amount, from_code, locale="ko_KR")} is ', end="")
print(
    f'{format_currency(exchage(from_code, to_code, amount), to_code, locale="ko_KR")}'
)
