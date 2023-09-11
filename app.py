from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/new")
def new():
    return render_template("new.html")


@app.route("/show")
def show():
    return render_template("show.html")


if __name__ == "__main__":
    app.run(debug=True)

data = request.form["テキストフィールド"]
