import json

import requests

result_list = []
catime = int(input("請輸入需要幾張貓咪圖片："))

for _ in range(catime):
    url = 'https://api.thecatapi.com/v1/images/search'
    resp = requests.get(url)
    json_resp = json.loads(resp.text)
    result_list.append(json_resp[0]['url'])

with open('cat_imgs.json', 'w', encoding='utf-8') as f:
    json.dump(result_list, f, indent=2, sort_keys=True, ensure_ascii=False)
