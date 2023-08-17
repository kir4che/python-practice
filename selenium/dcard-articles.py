import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge(
    '/Users/Molly/Desktop/Code/Python/edgedriver_mac64/msedgedriver.exe')
driver.get('https://www.dcard.tw/f')

scroll_time = int(input('請輸入捲動次數：'))
results = []
prev_element = None
for now_time in range(1, scroll_time+1):
    sleep(5)  # 等待其他文章載入
    elements = driver.find_elements(By.CLASS_NAME, 'sc-69e27e24-0')
    try:
        elements = elements[elements.index(prev_element):]
    except:
        pass
    for ele in elements:
        try:
            title = ele.find_element(By.CLASS_NAME, 'sc-69e27e24-2').text
            link = ele.find_element(
                By.CLASS_NAME, 'sc-69e27e24-2').get_attribute('href')
            print(f'{title}\n{link}\n\n')

            result = {
                'title': title,
                'link': link
            }
            results.append(result)
        except:
            pass
    prev_element = elements[-1]
    print(f"now scroll {now_time}/{scroll_time}")
    js = "window.scrollTo(0, document.body.scrollHeight);"
    driver.execute_script(js)

with open('dcard-articles.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2,
              sort_keys=True, ensure_ascii=False)

driver.quit()
