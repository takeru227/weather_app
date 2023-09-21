import numpy as np
from sklearn import svm

# csvファイルの読み込み
npArray = np.loadtxt("data_fuk.csv", delimiter=",", dtype="float")

# 説明変数の格納
x = npArray[:, 0:4]

# 目的変数の格納
y = npArray[:, 4:5].ravel()

# 学習手法にSVMを選択
model = svm.SVC()

# 学習
model.fit(x, y)

# 評価データ(ここは自分で好きな値を入力)
weather = [[9, 0, 7.9, 6.5]]

# predict関数で、評価データの天気を予測
ans = model.predict(weather)

if ans == 0:
    print("晴れです")
if ans == 1:
    print("曇りです")
if ans == 2:
    print("雨です")
