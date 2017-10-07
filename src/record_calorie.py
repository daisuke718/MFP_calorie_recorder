#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime

import unicodedata

def full2half(s):
    r = str(s)
    return r.translate(r.maketrans('０１２３４５６７８９−', '0123456789-'))


now = datetime.now()
today = now.strftime('%Y-%m-%d')
hour = now.hour
meal_default = -1
if 8 <= hour < 12:
    meal_default = 0
elif 12 <= hour < 15:
    meal_default = 1
elif 19 <= hour < 21:
    meal_default = 2
else:
    meal_default = 3

# 日付の指定
while True:
    print('日付を入力して下さい')
    print('デフォルト: ' + today)
    date = input('>>> ') or today
    try:
        date = full2half(date)
        print('入力日付: ' + date)
        datetime.strptime(date, '%Y-%m-%d')
        break
    except:
        print(sys.exc_info())
        continue

# 食事名の指定
while True:
    print('食事名を入力してください')
    print('0: 朝食, 1: 昼食, 2: 夕食, 3: おやつ')
    print('デフォルト: ' + str(meal_default))
    meal = input('>>> ') or meal_default
    try:
        meal = full2half(meal)
        print("入力食事名: " + str(meal))
        if int(meal) < 0 or 3 < int(meal):
            raise Exception
        break
    except:
        print(sys.exc_info())
        continue

while True:
    print('カロリーを入力してください(数値または計算式)')
    calorie = input('>>> ')
    try:
        calorie = full2half(calorie)
        calorie = int(eval(calorie))
        print('入力カロリー: ' + str(calorie))
        break
    except:
        print(sys.exc_info())
        continue
    
options = Options()
# ユーザディレクトリを固定
options.add_argument('user-data-dir=user-data-dir')
# ChromeのWebDriverオブジェクトを作成する
driver = webdriver.Chrome(chrome_options=options)

driver.get('http://www.myfitnesspal.com/ja/food/quick_add?meal=' + str(meal) + '&date=' + date)

# ユーザ＆パスワード保存のため、初回のみ必要
# el_username = driver.find_element_by_name('username')
# el_password = driver.find_element_by_name('password')
# 
# el_username.send_keys('')
# el_password.send_keys('')
# 
# el_password.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'quick-add-macros'))
)

el_calorie = driver.find_element_by_css_selector('input:nth-child(1)')
el_calorie.send_keys(calorie)

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary'))
)

el_submit_btn = driver.find_element_by_css_selector('.btn-primary')
el_submit_btn.click()

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'diary'))
)

driver.get(driver.current_url + "#main")

time.sleep(3)

driver.quit()
