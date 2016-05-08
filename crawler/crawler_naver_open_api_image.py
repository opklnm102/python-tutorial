# naver open api image download crawler

import urllib.parse
import urllib3
import re
import os

def input_query():
    q = urllib.parse.quote_plus(str(input("검색할 단어를 입력하세요: ")))
    return "&query=" + q

def bind_url():
    defult_url = "https://openapi.naver.com/v1/search/"
    target_image = "image.xml?"
    sort = "&sort=" + "sim"
    display = "&display=100"
    start = "&start=" + str(1)
    query = input_query()
    full_url = defult_url + target_image + sort + start + display + query
    return full_url

def fetch_contents_from_url():
    client_id = "gFoTYum7YnhIEoYLYGvc"
    client_serect = "yHxM2KTUIm"
    url = bind_url()
    http = urllib3.PoolManager()
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_serect}
    response = http.request('GET', url, headers=headers)
    result = response.data
    print(response.status)
    print(url)
    print(result)
    return result

def extract_text_in_tags(tags, tagname="title"):
    txt = []
    reg = "^[" + tagname + ">][^<]+"
    print(reg)
    for tag in tags:
        txt.append(re.search(reg, tag).group())
    print(txt)
    return txt


fetch_contents_from_url()








