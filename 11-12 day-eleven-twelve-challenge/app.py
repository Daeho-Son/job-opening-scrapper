from flask import Flask, render_template, request
from get_datas import get_subreddit


subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django",
]
subreddits = sorted(subreddits)
db = {}


app = Flask("DayEleven")


@app.route("/")
def home():
    return render_template("home.html", subreddits=subreddits)


@app.route("/read")
def read():
    name_keys = request.args.keys()
    subreddit_datas = []
    for name_key in name_keys:
        if name_key not in db.keys():
            db[name_key] = get_subreddit(name_key)
        subreddit_datas.append(db[name_key])
    subreddit_datas = sum(subreddit_datas, [])
    return render_template(
        "read.html", name_keys=request.args.keys(), subreddit_datas=subreddit_datas
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
