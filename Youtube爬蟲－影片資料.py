import random
import re
import time
from datetime import datetime

import pandas as pd
from tqdm import tqdm
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService


# 滾動頁面
def scroll(driver, xpathText):
    remenber = 0
    doit = True
    while doit:
        driver.execute_script("window.scrollBy(0,4000)")
        time.sleep(2)
        element = driver.find_elements(by=By.XPATH, value=xpathText)  # 抓取指定的標籤
        if len(element) > remenber:  # 檢查滾動後的數量有無增加
            remenber = len(element)
        else:  # 沒增加則等待一下，然後在滾動一次
            time.sleep(random.randint(5, 20))
            driver.execute_script("window.scrollBy(0,4000)")
            time.sleep(4)
            element = driver.find_elements(by=By.XPATH, value=xpathText)  # 抓取指定的標籤
            if len(element) > remenber:  # 檢查滾動後的數量有無增加
                remenber = len(element)
            else:
                doit = False  # 還是無增加，停止滾動
        time.sleep(2)
    return element  # 回傳元素內容


service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)
time.sleep(4)

# 抓取csv資料
getdata = pd.read_csv("Youtuber_頻道資料.csv", encoding="utf-8-sig")

# 準備容器
videoName = []
videoLink = []
commentNum = []
comment = []
for yName, yChannel, allLink in zip(
    getdata["Youtuber頻道名稱"], getdata["頻道網址"], getdata["所有影片連結"]
):
    print("開始爬取 " + yName + " 的影片")
    for link in tqdm(eval(allLink)):
        # 去到該影片
        driver.get(link)
        time.sleep(5)  # 網路慢的話這個最好長一點
        while (
            len(
                driver.find_elements(
                    by=By.XPATH,
                    value='//h1[@class="title style-scope ytd-video-primary-info-renderer"]',
                )
            )
            == 0
        ):
            time.sleep(2)
        videoLink.append(allLink)  # 取得影片連結

        # 2023/04/26更新，取得影片名稱
        getvideoName = driver.find_element(
            by=By.XPATH,
            value='//yt-formatted-string[@class="style-scope ytd-watch-metadata"]',
        ).text
        print("開始爬取： " + getvideoName)
        videoName.append(getvideoName)

        time.sleep(random.randint(2, 5))

        # 先滾動一小段在取得留言數
        while (
            len(
                driver.find_elements(
                    by=By.XPATH, value='//h2[@id="count"]/yt-formatted-string/span'
                )
            )
            == 0
        ):
            driver.execute_script(
                "window.scrollBy(0," + str(random.randint(30, 50)) + ")"
            )
            time.sleep(random.randint(2, 5))

        getcommentNum = driver.find_element(
            by=By.XPATH, value='//h2[@id="count"]/yt-formatted-string/span'
        ).text
        getcommentNum = getcommentNum.replace(",", "")
        commentNum.append(int(getcommentNum))  # 取得留言數

        # --- 開始進行「取得留言」工程
        # 滾動頁面
        getcomment = scroll(driver, '//div[@id="main"]')
        # 2023/05/10，抓不到發言者，發現標籤改為ID
        getfans = driver.find_elements(by=By.ID, value="author-text")  # 發言者

        # 儲存留言內容
        commentMan = []
        manChannel = []
        post_time = []
        comment_content = []
        comment_good = []

        count = 0  # 用來編號留言
        containar = []
        for fans, com in zip(getfans, getcomment):
            if count != 0:  # 第一次不需要執行，因為是youter自己的資料
                getcom = com.text
                getcom = getcom.replace("\n回覆", "")
                cutcom = getcom.split("\n")

                if len(cutcom) == 3:  # 若沒有人按讚，則補0
                    cutcom.append(0)
                try:
                    for i in range(2, len(cutcom) - 2, 1):
                        containar.append(cutcom[i])  # 留言內容
                except:  # 碰到異常資料之極端處理
                    containar["第" + str(count) + "筆留言資料"] = {"資料異常"}
            count += 1
        comment.append(containar)  # 儲存所有留言

    # 暫存器
    dic = {
        "影片名稱": videoName,
        "影片連結": videoLink,
        "留言數量": commentNum,
        "留言": comment,
    }

    # 使用 os 模組處理檔名，將非英文字符替換為下劃線 "_"
    file_name = str(yChannel) + "_Youtuber_影片資料.xlsx"
    file_name = "".join(c if c.isalnum() else "_" for c in file_name)

    # 使用 pandas.ExcelWriter 儲存為Excel檔案
    with pd.ExcelWriter(file_name, engine="openpyxl") as writer:
        pd.DataFrame(dic).to_excel(writer, index=False)

    print("頻道 " + str(yChannel) + " 爬取完成")

dic = {
    "影片名稱": videoName,
    "影片連結": videoLink,
    "留言數量": commentNum,
    "留言": comment,
}

# 使用 os 模組處理檔名，將非英文字符替換為下劃線 "_"
file_name = "Youtuber_影片資料.xlsx"

# 使用 pandas.ExcelWriter 儲存為Excel檔案
with pd.ExcelWriter(file_name, engine="openpyxl") as writer:
    pd.DataFrame(dic).to_excel(writer, index=False)
