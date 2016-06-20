# naver open api image download crawler

import urllib.parse  #url 검색어 인코딩에 쓰일 모듈
import urllib3
import re  #정규식
import os

#검색어 인코딩
def input_query():
    q = urllib.parse.quote_plus(str(input("검색할 단어를 입력하세요: ")))  #공백을 '+'로 치환
    return "&query=" + q

#요청 url 만들기
def bind_url():
    defult_url = "https://openapi.naver.com/v1/search/"
    target_image = "image.xml?"
    sort = "&sort=" + "sim"
    display = "&display=100"
    start = "&start=" + str(1)
    query = input_query()
    full_url = defult_url + target_image + sort + start + display + query
    return full_url

#url로 부터 contents를 가지고 온다.
def fetch_contents_from_url():
    client_id = "gFoTYum7YnhIEoYLYGvc"
    client_serect = "yHxM2KTUIm"
    url = bind_url()
    http = urllib3.PoolManager()
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_serect}
    response = http.request('GET', url, headers=headers)
    result = response.data  #data read
    print(response.status)  #확인
    print(url)  #확인
    print(result)  #확인
    return result

#html에서 꺼낸 태그들을 리스트로 넘겨주면 정규식을 사용해 텍스트만 남겨준다.
def extract_text_in_tags(tags, tagname="title"):
    txt = []
    reg = "[^<" + tagname + ">][^<]+"  #<title> xxxx... </title>면 '<title>'제외하고 '<'전까지 추출
    print(reg)  #확인
    for tag in tags:
        txt.append(re.search(reg, tag).group())
    print(txt)  #확인
    return txt

def get_contents_from_html():
    html = fetch_contents_from_url();
    title_tags = re.findall("<title>[^<]+</title>", html.decode('utf-8'))  #한글을 볼수 있게 decode
    link_tags = re.findall("<link>[^<]+</link>", html.decode('utf-8'))
    print("-------------------")
    #print(title_tags)  #확인
    #print(link_tags)  #확인

    #tag 내용 추출
    titles = extract_text_in_tags(title_tags, tagname = "title")
    links = extract_text_in_tags(link_tags, tagname = "link")

    # file에 쓰기
    f = open("image.html", "w")
    f.write("<html><body>")
    for i in range(1, len(titles)):
        f.write("<p>" + titles[i] + "</p>")
        f.write("<img src=" + links[i] + "/>")
    f.write("</body></html>")
    f.close()

get_contents_from_html()