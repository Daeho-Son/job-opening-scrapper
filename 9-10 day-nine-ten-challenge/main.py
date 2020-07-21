from flask import Flask, render_template, request
from get_datas import get_new, get_popular


db = {}
app = Flask("Day-Nine&Ten")


@app.route("/")
def index():
    return


app.run(host="0.0.0.0")
