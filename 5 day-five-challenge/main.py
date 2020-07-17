import os
from get_currency_codes import get_data as currency_codes
from check_number import check


os.system("clear")


data = currency_codes()
print("Hello! Please choose select a country by number:")
for count, data_i in enumerate(data):
    print(f"# {count} {data_i.get('country')}")


index = check(len(data))
print(f"You chose {data[index].get('country')}")
print(f"The currency code is {data[index].get('code')}")
