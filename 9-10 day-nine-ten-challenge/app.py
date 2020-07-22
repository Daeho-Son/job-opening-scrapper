from flask import Flask, render_template, request
from get_datas import get_new_popular, get_comment


db = {}
comment_db = {}
app = Flask("Day-Nine&Ten")


@app.route("/")
def index():
    order_by = request.args.get("order_by")
    if not order_by:
        order_by = "popular"

    db_data = db.get(order_by)
    if db_data:
        news_datas = db_data
    else:
        news_datas = get_new_popular(order_by)
        db[order_by] = news_datas
    return render_template("index.html", order_by=order_by, news_datas=news_datas)


@app.route("/<id>")
def detail(id):
    db_data = comment_db.get(id)
    if db_data:
        comment_data = db_data
    else:
        comment_data = get_comment(id)
        comment_db[id] = comment_data
    return render_template("detail.html", comment_data=comment_data)
