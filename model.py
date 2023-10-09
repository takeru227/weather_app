import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# csvファイルの読み込み
df = pd.read_csv("data_fuk.csv", delimiter=",", dtype="float")

# サンプルデータの用意
data = {
    "平均気温": [15, 18, 20, 22, 25],
    "降水量": [0, 20, 5, 1, 0],
    "日照時間": [5, 3, 8, 10, 12],
    "平均湿度": [60, 75, 50, 30, 25],
    "平均雲量": [30, 60, 20, 10, 5],
}
df = pd.DataFrame(data)

# 特徴量と目的変数に分割
X = df.drop("平均雲量", axis=1)
y = df["平均雲量"]

# データを訓練データとテストデータに分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# モデルの選択と訓練（ランダムフォレスト回帰モデルに変更）
model = RandomForestRegressor()
model.fit(X_train, y_train)

# 学習モデルの保存
with open("linear_regression_model.pkl", mode="wb") as file:
    pickle.dump(model, file)

# モデルのオープン
with open("linear_regression_model.pkl", mode="rb") as file:
    model = pickle.load(file)

# 新しいデータの作成
new_data = pd.DataFrame({"平均気温": [23], "降水量": [5], "日照時間": [9], "平均湿度": [45]})

# 新しいデータに対する予測
predicted_cloud_cover = model.predict(new_data)[0]


def predict(new_data):
    predicted_cloud_cover = model.predict(new_data)[0]
    return predicted_cloud_cover


print(f"Predicted Average Cloud Cover for New Data: {predicted_cloud_cover}")

# カテゴリ出力の処理
if predicted_cloud_cover <= 1:
    print("快晴")
elif 2 <= predicted_cloud_cover <= 8:
    print("晴れ")
else:
    print("曇り")
