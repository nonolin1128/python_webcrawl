# 抓取網頁原始碼
import urllib.request as req
url="https://www.mao-select.com.tw/mao/blog/"

# 定義爬蟲總頁數
total_pages = 7

# 迴圈爬多頁
for page in range(2, total_pages + 1):
    url = "https://www.mao-select.com.tw/mao/blog/?Prod_Mall_ID=mao&page={page}"

    # 建立一个 Request 物件，附加 Request Headers 的资讯
    request = req.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    })

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

# print(data)

#解析原始碼，取得資訊
import bs4
root=bs4.BeautifulSoup(data,"html.parser")
titles=root.find_all("div",class_="blog-text") #尋找 class="title"的div標籤
imgs=root.find_all("img",class_="blog-pic")
date=root.find_all("span",class_="blog-info-item")

for title in titles:
    if title.a != None:
        print(title.a.string)

for img in imgs:
    src = img.get("src")
    if src:
        print(src)

for span in date:
    text = span.text
    print(text)