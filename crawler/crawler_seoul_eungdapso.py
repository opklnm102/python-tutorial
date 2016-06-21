#서울시 응답소 페이지 크롤러

import os
import re
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

list_url = "http://eungdapso.seoul.go.kr/Shr/Shr01/Shr01_lis.jsp"
detail_url = "http://eungdapso.seoul.go.kr/Shr/Shr01/Shr01_vie.jsp"

#사용자에게 파일 저장경로를 입력받는다.
def get_save_path():
    save_path = str(input("저장할 위치와 파일명을 적어주세요: "))
    save_path = save_path.replace("\\", "/")  #'\'를 '/'로 교체

    if not os.path.isdir(os.path.split(save_path)[0]):  #디렉토리가 없으면 생성
        os.mkdir(os.path.split(save_path)[0])

    return save_path

#응답소의 민원 리스트페이스에서 민원들을 가져온다.
def fetch_list_url():
    request_header = urllib.parse.urlencode({"page": "1"})  #dict형태의 데이터를 인코딩된 문자열로 변환
    request_header = request_header.encode("utf-8")  #utf-8로 변환
    url = urllib.request.Request(list_url, request_header)
    response = urllib.request.urlopen(url).read().decode("utf-8")
    print(response)  #확인

    bs = BeautifulSoup(response, "html.parser")
    listbox = bs.find_all("li", class_="pclist_list_tit2")
    params = []
    for idx in listbox:  #detail을 위한 파라미터 추출
        #<a>의 href속성에서 0~9로 이루어진 14자리 숫자를 찾는다.
        params.append(re.search("[0-9]{14}", idx.find("a")["href"]).group())

    print(params)  #확인
    return params

#민원 내용이 들어있는 페이지를 열어 민원의 내용을 가져온다.
def fetch_detail_url():
    params = fetch_list_url()

    f = open(get_save_path(), 'w', encoding="utf-8")

    for p in params:

        request_header = urllib.parse.urlencode({"RCEPT_NO": str(p)})
        request_header = request_header.encode("utf-8")

        url = urllib.request.Request(detail_url, request_header)
        response = urllib.request.urlopen(url).read().decode("utf-8")

        #parsing
        bs = BeautifulSoup(response, "html.parser")
        div = bs.find("div", class_="form_table")

        tables = div.find_all("table")

        info = tables[0].find_all("td")

        title = info[0].get_text(strip=True)
        date = info[1].get_text(strip=True)

        question = tables[1].find("div", class_="table_inner_desc").get_text(strip=True)
        answer = tables[2].find("div", class_="table_inner_desc").get_text(strip=True)

        #file write
        f.write("==" * 30 + '\n')
        f.write(title + '\n')
        f.write(date + '\n')
        f.write(question + '\n')
        f.write(answer + '\n')
        f.write("==" * 30 + '\n')


fetch_detail_url()