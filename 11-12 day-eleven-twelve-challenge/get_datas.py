import requests
from bs4 import BeautifulSoup


"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""


def get_subreddit(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/top/?t=month"
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    datas = soup.select("div._1OVBBWLtHoSPfGCRaPzpTf > div.rpBJOHq2PR60pnwJlUyP0")
    subreddit_data = []
    for count, data in enumerate(datas[0].find_all("div", {"class": "scrollerItem"})):
        if data.find("span", {"class": "_2oEYZXchPfHwcf9mTMGMg8"}) == None:
            subreddit_data.append(
                {
                    "vote": data.find("div", {"class": "_23h0-EcaBUorIHC-JZyh6J"})
                    .find("div", {"class": "_1rZYMD_4xY3gRcSS3p8ODO"})
                    .text,
                    "title": data.find("div", {"class": "_1poyrkZ7g36PawDueRza-J"})
                    .find("h3", {"class": "_eYtD2XCVieq6emjKBH3m"})
                    .text,
                    "url": data.find("div", {"class": "_1poyrkZ7g36PawDueRza-J"}).find(
                        "a"
                    )["href"],
                    "word": subreddit,
                }
            )
    return subreddit_data
