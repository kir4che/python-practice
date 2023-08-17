import requests

# 對 google 發出 GET 請求

# 對 url 發出 GET 請求，並將回傳值存於 response。
res = requests.get('https://www.google.com')

# 等於下列
# res = requests.request('get', 'https://www.google.com')

# output：200
print(res.status_code)


# 添加參數

# 方法1
url = 'https://inshorts.deta.dev/news?category=technology'  # 直接把參數放到 url
res = requests.get(url)

# output：200
print(res.status_code)

# 方法2
url = 'https://inshorts.deta.dev/news'
params = {'category': 'technology'}
res = requests.get(url, params=params)

# output：200
print(res.status_code)


# 其他參數

url = 'https://inshorts.deta.dev/news?category=technology'  # 直接把參數放到 url
user_agent = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36 Edg/107.0.1418.42"
headers = {'user-agent': user_agent}
proxies = {'https': '76.72.138.48:3128'}

res = requests.get(url, headers=headers, proxies=proxies, verify=False)

# output：200
print(res.status_code)
