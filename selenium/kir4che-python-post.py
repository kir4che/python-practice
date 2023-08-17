from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge(
    '/Users/Molly/Desktop/Code/Python/edgedriver_mac64/msedgedriver.exe')
driver.get('https://kir4che.github.io')

# 搜尋文章
element = driver.find_element('id', 'search-input')
element.click()
search = driver.find_element('id', 'actual-search-input')
search.send_keys('Python')  # 搜尋有關 Python 的文章

# 要使用 By 請引入 from selenium.webdriver.common.by import By
element = driver.find_elements(By.CLASS_NAME, 'result-title')
for ele in element:
    print(ele.text)

driver.quit()
