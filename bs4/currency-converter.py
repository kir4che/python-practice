import requests
from bs4 import BeautifulSoup

currency = input('請輸入您要查詢的幣種匯率：')
url = f'https://www.google.com/search?q={currency}'  # 查詢匯率

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
res = requests.get(url, headers={
    'user-agent': user_agent
})
soup = BeautifulSoup(res.text, 'html.parser')

forex_rate = soup.find('span', class_='DFlfde SwHCTb')
# 真正的貨幣名稱可能跟自己搜尋的有差，所以再取得一次。
currency = soup.find('span', class_='vLqKYe')['data-name']

print(f'目前 1 {currency} ＝ 新台幣 {forex_rate.text} 元')

amount = input(f'請問您要換多少{currency}？')

# 注意型態要一樣才能相加
exchanged_amount = float(amount) * float(forex_rate.text)

print(f'目前 {amount} {currency} ＝ 新台幣 {exchanged_amount} 元')
