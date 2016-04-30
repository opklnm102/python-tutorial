

import urllib.request

# 웹문서 불러오기
req = urllib.request  #웹을 열어서 데이터를 읽어오는 기능
d = req.urlopen("http://www.naver.com")  #웹에서 얻은 데이터 객체를 돌려준다.
print(d)

# 웹서버 정보 받아오기
status = d.getheaders()  #서버에 대한 정보를 얻는다.
for s in status:
    print(s)

print(d.status)  #웹페이지 상태 코드 확인하기

# 웹페이지의 데이터를 읽어오기
print(d.read())  #HTML을 읽는다.

import urllib.parse  #인코딩 모듈

# 한글 검색어 인코딩
# quote() - 공백을 '%20', quote_plus() - 공백을 '+'로 인코딩. quote_plus()권장
def input_query():
    q = urllib.parse.quote_plus(str(input("검색어를 입력하세요: ")))
    return "&query=" + q

query = input_query()
print(query)