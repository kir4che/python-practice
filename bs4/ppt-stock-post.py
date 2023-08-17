import json

import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/Stock'
article_list = []  # 新增一陣列以備存放所有文章的資訊


def get_res(url):
    res = requests.get(url)
    # 該網址無效則回傳 error
    return res if res.status_code == 200 else 'Error!'


def get_articles(res):
    soup = BeautifulSoup(res.text, 'html.parser')

    titles = soup.find_all('div', class_='r-ent')
    for i in titles:
        if i.find('a') != None:
            title = i.find('a').get_text()
            # 如果文章被刪除則跳過此次迴圈
            if not title.startswith('(本文已被刪除)'):
                link = 'https://www.ptt.cc' + i.find('a')['href']
                # 將每一文章資訊存為一個字典，並將其存入 article_list。
                article = {
                    'title': title,
                    'link': link
                }
                article_list.append(article)
                # print(f'title：{title}\nlink：{link}\n')
            else:
                pass
    # 取得下一頁的網址
    next_url = 'https://www.ptt.cc' + \
        soup.select_one(
            '#action-bar-container > div > div.btn-group.btn-group-paging > a:nth-child(2)')['href']
    return next_url


total_page_num = 3
for now_page_num in range(total_page_num):
    # print(f'crawing：{url}\n')
    res = get_res(url)
    if res != 'Error!':
        url = get_articles(res)
        # print(f'----------{now_page_num+1}/{total_page_num}----------')

with open('ptt-stock-articles.json', 'w', encoding='utf-8') as f:
    json.dump(article_list, f, indent=2,
              sort_keys=True, ensure_ascii=False)

# print(article_list)
