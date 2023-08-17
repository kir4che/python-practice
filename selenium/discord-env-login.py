import os
from time import sleep

from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By

# 讀取環境變數
load_dotenv()
email = os.getenv('email')
password = os.getenv('password')

driver = webdriver.Edge(
    '/Users/Molly/Desktop/Code/Python/edgedriver_mac64/msedgedriver.exe')
driver.get(
    'https://discord.com/login?redirect_to=%2Fchannels%2F868043633197195314%2F874469620164227143')
sleep(1)

# 輸入帳號、密碼
driver.find_element(By.ID, 'uid_5').send_keys(email)
driver.find_element(By.ID, 'uid_8').send_keys(password)
# 按下登入按鈕
driver.find_element(
    By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/button[2]').click()
sleep(10)
