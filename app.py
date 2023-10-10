from flask import Flask, render_template
from flask import request
from model import predict
import numpy as np
import pandas as pd

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
        return render_template("show.html")
    # POSTの処理
    elif request.method == "POST":
        average_temperature = request.form["average temperature"]
        Precipitation = request.form["Precipitation"]
        sunshine_hours = request.form["sunshine hours"]
        average_humidity = request.form["average humidity"]
        data = [average_temperature, Precipitation, sunshine_hours, average_humidity]
        data_int = [int(d) for d in data]
        answer = pd.DataFrame(
            {
                "平均気温": [data_int[0]],
                "降水量": [data_int[1]],
                "日照時間": [data_int[2]],
                "平均湿度": [data_int[3]],
            }
        )
        result = predict(answer)
        return render_template("show.html", text=data, result=result)


if __name__ == "__main__":
    app.run(debug=True)
