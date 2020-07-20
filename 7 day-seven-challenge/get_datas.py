import requests
from bs4 import BeautifulSoup


def get_alba_superbrands():
    alba_url = "http://www.alba.co.kr"
    alba_soup = BeautifulSoup(requests.get(alba_url).text, "html.parser")
    li_a = alba_soup.select("div#MainSuperBrand > ul.goodsBox > li > a.goodsBox-info")

    brands = []
    for a in li_a:
        brand_name = a.find("span", {"class": "company"}).text
        brand_url = a["href"]
        print(f"{brand_name} : {brand_url}")
        brands.append(
            {
                "brand_name": brand_name,
                "brand_recruits": get_brand_recruits(brand_name, brand_url),
            }
        )

    return brands


def get_brand_recruits(brand_name, url):
    recruits = []
    page_count = 0
    while True:
        page_count += 1
        if brand_name == "ELAND FASHION":
            brand_url = url + f"?page={page_count}"
        else:
            brand_url = url + f"job/brand/?page={page_count}"
        brand_soup = BeautifulSoup(requests.get(brand_url).text, "html.parser")
        tr = brand_soup.select("div#NormalInfo > table > tbody > tr")
        if tr[0].find("td").text == "해당 조건/분류에 일치하는 채용정보가 없습니다.":
            break
        print(f"{brand_name} 일반 채용정보 {page_count} 페이지 가져오는 중...")
        for count, tr_i in enumerate(tr):
            if count % 2 == 0:
                td = tr_i.find_all("td")
                recruits.append(
                    {
                        "place": td[0].text.replace("\xa0", " "),
                        "title": td[1].find("span", {"class": "company"}).text,
                        "time": td[2].find("span").text,
                        "pay": td[3].find("span", {"class": "payIcon"}).text
                        + td[3].find("span", {"class": "number"}).text,
                        "date": td[4].text,
                    }
                )
    print(f"{brand_name}의 모든 페이지에서 일반 채용정보 가져오기 완료.")
    print("\n" + "=" * 50 + "\n")
    return recruits
