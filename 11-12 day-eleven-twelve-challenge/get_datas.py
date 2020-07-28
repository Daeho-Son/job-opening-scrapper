import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
}


def get_subreddit(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/top/?t=month"
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    datas = soup.select("div._1OVBBWLtHoSPfGCRaPzpTf > div.rpBJOHq2PR60pnwJlUyP0")
    subreddit_data = []
    for data in datas[0].find_all("div", {"class": "scrollerItem"}):
        if data.find("span", {"class": "_2oEYZXchPfHwcf9mTMGMg8"}) == None:
            subreddit_data.append(
                {
                    "vote": data.select(
                        "div._23h0-EcaBUorIHC-JZyh6J div._1rZYMD_4xY3gRcSS3p8ODO"
                    )[0].text,
                    "title": data.select(
                        "div._1poyrkZ7g36PawDueRza-J h3._eYtD2XCVieq6emjKBH3m"
                    )[0].text,
                    "url": data.select("div._1poyrkZ7g36PawDueRza-J a")[0]["href"],
                    "word": subreddit,
                }
            )
    return subreddit_data
