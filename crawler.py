import urllib.request as req
import pandas as pd

# 抓取網頁原始碼
url="https://www.mao-select.com.tw/mao/blog-detail/%E6%AF%9B%E5%AD%A9%E6%88%91%E8%B7%9F%E4%BD%A0%E8%AA%AA/%E6%AF%9B%E5%AD%A9%E7%9F%A5%E8%AD%98/%E4%BD%95%E8%AC%82%E5%A4%A9%E7%84%B6%E8%B1%86%E8%85%90%E7%A0%82%EF%BC%9A%E8%AE%93%E8%B2%93%E5%92%AA%E6%93%81%E6%9C%89%E8%88%92%E9%81%A9%E5%A6%82%E5%BB%81%E9%AB%94%E9%A9%97/"

#建立一個 Request 物件，附加 Request Headers 的資訊
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
# print(data)

#解析原始碼，取得資訊
import bs4
root=bs4.BeautifulSoup(data,"html.parser")
titles=root.find_all("div",class_="blog-text") #尋找 class="title"的div標籤
imgs=root.find_all("img",class_="blog-pic")
date=root.find_all("span",class_="blog-info-item")
words=root.find_all("p",class_="p2")
tags=root.find_all("li",class_="blog-tag")


# for title in titles:
#     if title.a != None:
#         print(title.a.string)

# for img in imgs:
#     src = img.get("src")
#     if src:
#         print(src)

# for span in date:
#     text = span.text
#     print(text)

for tag in tags:
    if tag.a != None:
        print(tag.a.string)