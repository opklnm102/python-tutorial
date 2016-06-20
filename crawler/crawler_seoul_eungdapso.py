#서울시 응답소 페이지 크롤러

import urllib3
from bs4 import BeautifulSoup
import re
import os

list_url = "http://eungdapso.seoul.go.kr/Shr/Shr01/Shr01_lis.jsp"
detail_url = "http://eungdapso.seoul.go.kr/Shr/Shr01/Shr01_vie.jsp"

def get_save_path():
    save_path = str(input("저장할 위치와 파일명을 적어주세요: "))
    save_path = save_path.replace("\\", "/")

    if not os.path.isdir(os.path.split(save_path)[0]):
        os.mkdir(os.path.split(save_path)[0])

    return save_path

def fetch_list_url():
    request_header = urllib