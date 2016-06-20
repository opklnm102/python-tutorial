# naver open api news search crawler

import urllib3
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
print(fullURL)  #확인
cwd = os.getcwd()  #현재 디렉토리에 저장하기 위해
print(cwd)  #확인

file = open("naver_news.txt", "w", encoding='utf-8')  #파일 열기

http = urllib3.PoolManager()
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_serect}
response = http.request('GET', fullURL, headers=headers)
print("statscode= " + str(response.status))  #status code 확인

resultXML = response.data  #read data
#print(response.data)  #확인
xmlsoup = BeautifulSoup(resultXML, 'html.parser')  #parse

items = xmlsoup.find_all('item')  #item태그를 모두 가져와서 리스트로 저장


for item in items:
    print(item)
    file.write("-----------------------------------------------------\n")
    file.write("news title: " + item.title.get_text(strip=True) + '\n')  #텍스트들을 공백제거하고 저장
    file.write("description: " + item.description.get_text(strip=True) + '\n')
    file.write("link: " + item.link.get_text(strip=True) + '\n')
    file.write('\n')

file.close()