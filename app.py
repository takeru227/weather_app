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

        if result <= 1:
            message = "快晴"
        elif 2 <= result <= 8:
            message = "晴れ"
        else:
            message = "曇り"

        if data_int[0] < 5:
            temperature = "ダウンコートがおすすめ"
        elif 5 <= data_int[0] < 10:
            temperature = "冬物コートがおすすめ"
        elif 10 <= data_int[0] < 15:
            temperature = "セーターやトレンチコートがおすすめ"
        elif 15 <= data_int[0] < 20:
            temperature = "長袖＋カーディガンがおすすめ"
        elif 20 <= data_int[0] < 25:
            temperature = "長袖がおすすめ"
        else:
            temperature = "半袖がおすすめ"

        return render_template(
            "show.html",
            text=data,
            result=result,
            message=message,
            temperature=temperature,
        )


if __name__ == "__main__":
    app.run(debug=True)
