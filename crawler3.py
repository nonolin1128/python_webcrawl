import urllib.request as req
import pandas as pd

# 建立一個空的DataFrame
df = pd.DataFrame(columns=["titles", "imgs", "date"])

# 抓取網頁原始碼
url="https://www.mao-select.com.tw/mao/blog/"

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



# 把數據丟進去
for title, img, span in zip(titles, imgs, date):
    title_text = title.a.string.strip() if title.a else ""
    img_src = img.get("src") if img.has_attr("src") else ""
    date_text = span.text.strip()
    df = df.append({"titles": title_text, "imgs": img_src, "date": date_text}, ignore_index=True)

# 儲存
df.to_excel("blog_data.xlsx", index=False)