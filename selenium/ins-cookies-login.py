import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

# 取得已登入的 IG cookies
with open('ins_cookies.json') as f:
    cookies = json.load(f)

driver = webdriver.Edge(
    '/Users/Molly/Desktop/Code/Python/edgedriver_mac64/msedgedriver.exe')
driver.get('https://www.instagram.com')

# 添加 cookies
for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()
sleep(10)
