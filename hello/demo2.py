import requests
from bs4 import BeautifulSoup

adress_num = []

# 设置请求头，模拟浏览器请求
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
for page in range(1, 71):
    url = f"https://xc8866.cc/forum-46-{page}.htm?orderby=lastpid&digest=0"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    adress = soup.find_all("li", class_=["media", "thread","tap"])

    for i in adress:
        aa = i.get("data-tid")
        adress_num.append(aa)

print(adress_num)
with open("demo11.txt", "a") as file:
    for i in adress_num:
        url1 = f"https://xc8866.cc/thread-{i}.htm"
        response1 = requests.get(url1, headers)
        soup = BeautifulSoup(response1.text, "html.parser")
        text1 = soup.select("strong[data-darkreader-inline-color='']")
        text2 = soup.select("span[data-darkreader-inline-color='']")
        text3 = soup.find_all("img", class_='img-fluid')
        # print (len(text1))
        # print(len(text2))
        # for b in text1:
        #     print(b.text)
        for a in text2:
            file.write(a.text+"\n")
        for b in text3:
            print(b.get('src'))
            file.write(b.get("src")+"\n")

