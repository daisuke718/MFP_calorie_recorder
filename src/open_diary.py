#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# ユーザディレクトリを固定
options.add_argument('user-data-dir=user-data-dir')
# ChromeのWebDriverオブジェクトを作成する
driver = webdriver.Chrome(chrome_options=options)

driver.get('http://www.myfitnesspal.com/food/diary#main')

time.sleep(30)

driver.quit()
