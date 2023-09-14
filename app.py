from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/new")
def new():
    return render_template("new.html")


@app.route("/show", methods=["GET", "POST"])
def show():
    # GETの処理
    if request.method == "GET":
        print("get method!")
        return render_template("show.html")
    # POSTの処理
    elif request.method == "POST":
        print("post method!")
        text = "hello"
        return render_template("show.html", text=text)


if __name__ == "__main__":
    app.run(debug=True)

data = request.form["text field"]
