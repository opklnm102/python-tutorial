# naver open api news search crawler

import urllib3
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import os

defaultURL = "https://openapi.naver.com/v1/search/"
client_id = "gFoTYum7YnhIEoYLYGvc"
client_serect = "yHxM2KTUIm"
target_news = "news.xml?"
target_blog = "blog.xml?"
sort = "&sort=sim"
display = "&display=100"
start = "&start=1"
query = "query=" + urllib.parse.quote_plus(str(input("검색어를 입력하세요: ")))

fullURL = defaultURL + target_blog + query + sort + display + start
print(fullURL)
cwd = os.getcwd()
print(cwd)

file = open("naver_news.txt", "w", encoding='utf-8')

http = urllib3.PoolManager()
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_serect}
response = http.request('GET', fullURL, headers=headers)
print("statscode= " + str(response.status))

resultXML = response.data
#print(response.data)
xmlsoup = BeautifulSoup(resultXML, 'html.parser')

items = xmlsoup.find_all('item')


for item in items:
    print(item)
    file.write("-----------------------------------------------------\n")
    file.write("news title: " + item.title.get_text(strip=True) + '\n')
    file.write("description: " + item.description.get_text(strip=True) + '\n')
    file.write('\n')

file.close()