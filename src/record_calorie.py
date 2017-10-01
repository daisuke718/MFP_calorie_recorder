#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime

today = datetime.now().strftime('%Y-%m-%d')

print('日付を入力して下さい')
print('デフォルト: ' + today)
date = input('>>> ') or today

print('食事名を入力してください')
print('0: 朝食, 1: 昼食, 2: 夕食, 3: おやつ')
meal = input('>>> ')

while True:
    print('カロリーを入力してください(数値または計算式)')
    calorie = input('>>> ')
    try:
        calorie = eval(calorie)
        print('入力カロリー: ' + str(calorie))
        break
    except:
        continue
    
options = Options()
# ユーザディレクトリを固定
options.add_argument('user-data-dir=user-data-dir')
# ChromeのWebDriverオブジェクトを作成する
driver = webdriver.Chrome(chrome_options=options)

driver.get('http://www.myfitnesspal.com/ja/food/quick_add?meal=' + meal + '&date=' + date)

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

driver.quit()
