import os
import requests
import sys


os.system("clear")


def check_url(url_list):
    for url in url_list:
        url = url.strip().lower()
        if ".co" not in url:
            print(f"{url} is not a valid URL.")
            pass
        else:
            url = (
                f'https:{url.replace(url[: url.find(":") + 1], "").replace(" ", "")}'
                if url.find(":") != -1
                else f'https://{url.replace(" ","")}'
            )
            try:
                print(
                    (f"{url} is down!", f"{url} is up!")[
                        requests.get(url).status_code == requests.codes.ok
                    ]
                )
            except requests.ConnectionError:
                print(f"{url} is down!")
    if recursion() == "n":
        return 0


def recursion():
    re = input("Do you want to start over? y/n ")
    if (re != "y") and (re != "n"):
        print("That's not a valid answer")
        recursion()
    else:
        return re


print("Welcome to IsItDown.py!")
print("Please write a URL or URLs you want to check. (separated by comma)")
while 1:
    if check_url(sys.stdin.readline().split(",")) == 0:
        print("S .bye!")
        break
