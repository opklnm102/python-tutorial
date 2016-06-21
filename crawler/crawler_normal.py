#일반 홈페이지 크롤러

#방법
#1. 게시물의 목록들이 어느 태그에 속하는지 확인하고 그 태그를 BeautifulSoup를 이용 parsing
#2. 게시물의 목록을 가지고 있는 태그에서 게시물들의 제목에 있는 게시물 콘텐츠 url을 가져온다.

#실행 순서
#1. fetch_post_list()로부터 게시물의 목록 얻기
#2. 데이터를 저장할 텍스트 파일 'w'모드로 open
#3. fetch_post_list()로 얻어낸 리스트들을 fetch_post_contents()에 넣어 내용 추출
#4. 추출한 내용을 파일에 구분하여 저장하고 이미지 저장
#5. 텍스트 파일 저장하고 종료

import urllib3
from bs4 import BeautifulSoup

target_url = "http://52.68.130.249/textboard/"

#게시글의 제목과 목록을 가져온다.
def fetch_post_list():
    http = urllib3.PoolManager()
    response = http.request('GET', target_url)  #request
    html = response.data

    #parsing
    bs = BeautifulSoup(html, 'html.parser')
    table = bs.find('table', class_='kingkongboard-table')  #find(tag, class)
    title_list = table.find_all('td', class_='kingkongboard-list-title')
    links = [td.find('a')['href'] for td in title_list]  #title_list에서 <a href='xx'/>를 찾아 리스트로 만든다.
    #print(links)  #확인
    return links

#게시글의 세부 내용을 가져온다.
def fetch_post_contents(link):
    url = link
    http = urllib3.PoolManager()
    response = http.request('GET', url)  #request
    html = response.data

    #parsing
    bs = BeautifulSoup(html, 'html.parser')
    content_table = bs.find('div', id='kingkongboard-read-table')

    #글제목, 등록 날짜 가져온다.
    title_section = content_table.find('div', class_='title-section')
    title = title_section.find('h1').text
    date = title_section.find('div', class_='regist-date').find('h2').text

    #글쓴이 정보
    writer = content_table.find('div', class_='regist-writer').find('h2').text

    #콘텐츠 정보
    content = content_table.find('div', class_='content-section').find('p').text

    #이미지 정보
    image = content_table.find('div', class_='content-section').find('img')
    image_url = ''
    if image:  #image tag를 찾았다면 src추출
        image_url = image['src']

    #댓글 정보
    comments = []
    comment_section = content_table.find('div', class_='comment-section')
    list_wrapper = comment_section.find('div', class_='list-wrapper')
    comment_list = list_wrapper.find_all('div', class_='each-comment')  #each-comment comment-2, each-comment comment-3...
    if comment_list:
        for comment in comment_list:
            comment_box = comment.find('div', class_='comment-box')
            comment_content = comment_box.find('div', class_='comment-content')

            div_writer = comment_content.find('div', class_='comment-content-writer')
            writer = div_writer.find('span', class_='author').text
            date = div_writer.find('span', class_='date').text

            div_text = comment_content.find('div', class_='comment-content-text')
            comment_text = div_text.find('h2').text

            comments.append({
                'writer': writer,
                'date': date,
                'comment_text': comment_text
            })

    return {
        'title': title,
        'date': date,
        'writer': writer,
        'content': content,
        'image': image_url,
        'comments': comments
    }

#크롤링한 내용을 파일로 저장
def crawler_running():
    links = fetch_post_list()  #게시물 목록 가져오기
    with open('post.txt', 'w', encoding='utf-8') as f:  #file open
        for link in links:
            result = fetch_post_contents(link)  #내용 가져오기
            print(result)  #확인
            f.write("==" * 30 + '\n')
            f.write("글 제목: " + result['title'] + '\n')
            f.write("날짜: " + result['date'] + '\n')
            f.write("글쓴이: " + result['writer'] + '\n')
            f.write("글 내용: " + result['content'] + '\n')

            if result['comments']:
                f.write('-' * 30)
                f.write('댓글')
                f.write('-' * 30 + '\n')
                count = 1
                for comment in result['comments']:
                    f.write('댓글' + str(count) + '\n')
                    f.write('댓글 작성자: ' + comment['writer'] + '\n')
                    f.write('댓글 등록 날짜: ' + comment['date'] + '\n')
                    f.write('댓글 내용' + comment['comment_text'] + '\n')
                    count += 1
            f.write('===' * 30 + '\n')

            if result['image']:
                image = open(result['title'] + '.jpg', 'wb')
                http = urllib3.PoolManager()
                down_img = http.request('GET', result['image'])
                image.write(down_img.data)
                image.close()
        f.close()

crawler_running()



