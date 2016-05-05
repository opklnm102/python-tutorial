# -*- coding: utf-8 -*-

# beautifulsoup test
from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()
response = http.request('GET', "http://www.naver.com")
print(response.status)

bs = BeautifulSoup(response.data)
print(bs.prettify())
print()

# find() - 태그를 하나만 가저온다. 없으면 안나온다.
print(bs.find('p'))
print(bs.find('title'))
print(bs.find('button', type='button'))  # 속성조회 속성이름="값"
print()

# find_all() - 해당 태그가 여러개 있을 경우 한꺼번에 모두 가져온다.
print(bs.find_all('p'))  # 자신의 태그안에 있는 것만 가져온다.
print()

# 여러가지 태그를 찾아야하는 상황, p,img태그를 같이 찾고 싶을 때
body_tag = bs.find('body')
tag_list = body_tag.find_all(['p', 'img'])  #인수에 리스트

for tag in tag_list:
    print(tag)

bs.find_all('a')  #인수에 문자열
bs.find_all(['p', 'img'])  #인수에 리스트

import re
print(bs.find_all(re.compile("^p")))  #인수에 정규식
print()

# 인수에 속성
print(bs.find_all(align="center"))
print(bs.find_all(width="500"))
print()

# text인수 - 문자열, 정규식, 리스트 등 전달 가능
bs.find_all(text="text contents 1")  #문장이 "text contents 1"인 태그를 찾는다.
bs.find_all(text=re.compile(" text +"))   #"text "이후 임의의 한문자가 존재하는 태그를 찾는다.

# limit인수 - 태그의 개수 제한
print(bs.find_all('p', limit=2))
print()

# 문장 가져오기










