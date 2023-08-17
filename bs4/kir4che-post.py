import requests
from bs4 import BeautifulSoup

url = 'https://kir4che.github.io/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# 取得網站標題
title = soup.find('title')
print(title)  # <title>kir4che</title>

# 取得第一篇文章標題
post_title = soup.find('a', class_='article-title').string
print(post_title)  # [React x SpringBoot] 電商平台－查詢訂單列表

# 取得第一頁的所有文章標題
post_titles = soup.find_all('a', class_='article-title')
for i in post_titles:
    print(i.string)
    # 取得該文章的網址
    print('https://kir4che.github.io' + i['href'], end='\n\n')
