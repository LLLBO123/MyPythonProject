# import requests
# from bs4 import BeautifulSoup
#
# # 设置请求头，模拟浏览器请求
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
# }
# #
# # for page in range(1, 71):
# #     url = f"https://xc8866.cc/forum-46-{page}.htm?orderby=lastpid&digest=0"
# #     response = requests.get(url, headers=headers)
# #     soup = BeautifulSoup(response.text, "html.parser")
# #     web_adress = soup.find_all("li", class_='media thread tap ')
# #     pass
#
# # url = 'https://xc8866.cc/thread-16797.htm'
# # 循环获取每一页的电影数据
# for page in range(0, 250, 25):
#     url = f"https://movie.douban.com/top250?start={page}&filter="
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.text, "html.parser")
#     movies = soup.find_all("div", class_="info")
#
#     # 循环获取每一部电影的详细信息并打印
#     for movie in movies:
#         title = movie.find("span", class_="title").get_text()
#         # year = movie.find("span", class_="year").get_text()
#         rating = movie.find("span", class_="rating_num").get_text()
#         quote = movie.find("span", class_="inq")
#         if quote:
#             quote = quote.get_text()
#         else:
#             quote = "暂无评价"
#         print(f"{title}：{rating}，{quote}")


