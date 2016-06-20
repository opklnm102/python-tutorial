# Daum open api를 이용한 특정 검색어로 기사 검색 크롤러

from bs4 import BeautifulSoup
import urllib.parse
import urllib3
import os

apikey = "b50800d7b3da504f9054322217b19c9b"
default_url = "https://apis.daum.net/search/web?output=xml&apikey="

#저장위치 선택
def get_save_path():
    save_path = str(input("저장할 위치와 파일명을 적어주세요: "))
    save_path = save_path.replace("\\","/")  # '\'을 '/'로 교체
    if not os.path.isdir(os.path.split(save_path)[0]):  # 없는 디렉토리면 생성
        os.mkdir(os.path.split(save_path)[0])
    return save_path

#요청 결과 반환
def get_result_xml():
    search = urllib.parse.quote_plus(str(input("검색할 문장을 입력하세요: ")))  #검색어 utf-8로 변환
    full_url = default_url + apikey + '&q=' + search
    http = urllib3.PoolManager()
    response = http.request('GET', full_url)  #요청
    result = response.data  #결과 추출
    print(response.status)
    print(result)
    return result

#xml결과 파일로 저장
def fetch_result_xml():
    result_xml = get_result_xml()
    bs = BeautifulSoup(result_xml, 'html.parser')
    items = bs.find_all("item")  #item 태그 찾기
    print(items)
    f = open(get_save_path(), 'w', encoding='utf-8')

    #item태그에서 원하는 태그 추출해서 파일로 저장
    for item in items:
        date = item.find("pubdate").get_text(strip=True)  #pubdata태그에서 내용만 공백제거해서 가저온다.
        title = item.find("title").get_text(strip=True)
        desc = item.find("description").get_text(strip=True)
        link = item.find("link").get_text(strip=True)
        url = item.find("url").get_text(strip=True)
        f.write("==" * 30 + '\n')
        f.write("게시물 날짜: " + date + '\n')
        f.write("제목: " + title + '\n')
        f.write("설명: " + desc + '\n')
        f.write("링크: " + link + '\n')
        f.write("URL: " + url + '\n')

        f.write("==" * 30 + '\n')

fetch_result_xml()
