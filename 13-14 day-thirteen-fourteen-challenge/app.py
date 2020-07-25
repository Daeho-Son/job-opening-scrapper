from flask import Flask, render_template, request
from get_datas import get_job_datas


db = {}


app = Flask("Day-Thirteen-Fourteen")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def jobs():
    term = request.args.get("term")
    if term in db:
        job_datas = db.get("term")
    else:
        job_datas = get_job_datas(term)
        db[term] = job_datas
    return render_template("jobs.html", term=term)


@app.route("/download")
def download():
    return

