# MFP_calorie_recorder
MyFitnessPalのカロリー入力を自動化するスクリプト。
カロリー追加ページ表示が遅いことの解決として作りました。

# インストール

## 前提
- python3系がインストールされていること
- chromeDriverがインストールされていること(https://sites.google.com/a/chromium.org/chromedriver/)

## 環境構築手順
```
$ git clone git@github.com:daisuke718/MFP_calorie_recorder.git
$ cd MFP_calorie_recorder
$ python3 -m venv .
$ source bin/activate
$ pip install -r requirements/requirements.txt
```

## 初回実行
MFPのユーザ・パスワードを記憶させるため、初回はソースコードのコメントアウトを外して実行する必要があります。
（2回目以降、入力したユーザ・パスワードはカレントディレクトリのuser-data-dirに保存されます）

# 使い方

```
$ cd MFP_calorie_recorder
$ source bin/activate
$ src/record_calorie.py
```

あとは画面の指示に従って入力してください
