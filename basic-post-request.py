import json

import requests

# 字典
url = 'https://zh.wikipedia.org/'
data = {
    'account': 'test123',
    'password': 'test123'
}
res = requests.post(url, data=data)

print(res.status_code)

# JSON
url = 'https://zh.wikipedia.org/'
data = json.dumps(data)
res = requests.post(url, data=data)

print(res.status_code)
