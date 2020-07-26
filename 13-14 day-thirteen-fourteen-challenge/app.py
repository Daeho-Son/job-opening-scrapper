from flask import Flask, render_template, request, redirect
from get_datas import get_job_datas
from exporter import export_to_file

db = {}


app = Flask("Day-Thirteen-Fourteen")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search")
def jobs():
    try:
        term = request.args.get("term")
        if not term:
            raise Exception()
        term = term.lower()
        job_datas = db.get(term)
        if not job_datas:
            job_datas = get_job_datas(term)
            db[term] = job_datas
    except:
        return redirect("/")
    return render_template(
        "jobs.html", term=term, job_datas=job_datas, count_job_datas=len(job_datas)
    )


@app.route("/export")
def export():
    try:
        term = request.args.get("term")
        if not term:
            raise Exception()
        term = term.lower()
        job_datas = db.get(term)
        if not job_datas:
            job_datas = get_job_datas(term)
            db[term] = job_datas
        export_to_file(job_datas)
    except:
        return redirect("/")
    return redirect("/")
