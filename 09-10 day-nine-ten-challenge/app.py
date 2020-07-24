import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"
new_url = f"{base_url}/search_by_date?tags=story"
popular_url = f"{base_url}/search?tags=story"

db = {}
app = Flask("DayNine")


@app.route("/")
def index():
    order_by = request.args.get("order_by", "popular")
    # request.args에서 oder_by를 찾고 그 초기값을 popular로 정함
    check_db = db.get(order_by)
    if check_db:
        story_datas = check_db
    else:
        if order_by == "popular":
            story_datas = requests.get(popular_url).json().get("hits")
        elif order_by == "new":
            story_datas = requests.get(new_url).json().get("hits")
        db[order_by] = story_datas
    return render_template("index.html", story_datas=story_datas, order_by=order_by)


@app.route("/<id>")
def detail(id):
    detail_url = f"{base_url}/items/{id}"
    detail_data = requests.get(detail_url).json()
    return render_template("detail.html", detail_data=detail_data)
