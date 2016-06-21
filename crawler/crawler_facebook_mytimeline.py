#facebook 나의 게시물 가져오기
#posts는 내가 작성한 글만 내 타임라인에서 가져온다. 다른 사람이 남긴 글까지 보고 싶다면 feed 사용

#pip3 install facebook-sdk
import facebook
import os

obj = facebook.GraphAPI(access_token="EAACEdEose0cBAO0nNA7phdZCnzTYBeHaJO415GcEEKJQV8mOeZAzMYhI6ryrZCt5oAgOWxWlVuRSt42kj1DzZBLNj7jFXpQJXtCbGOiUtmfoOrVoqR5EVR26v8atnZCxFHCGBuIhgnvuwJuHON5PwRx61nzJ8th4N1LelMlvWrwZDZD")
limit = int(input("몇건의 게시물을 검색할까요?"))
response = obj.get_connections(id="me", connection_name="posts", limit=limit)  #나의 게시물을 가져온다.
f = open(os.getcwd() + "/posts.txt", "w")

print(response[u"data"])

for data in response[u"data"]:
    f.write("==" * 30 + "\n")
    f.write("게시물 작성자: " + data[u"from"][u"name"].encode("utf-8").decode() + "\n")
    f.write("게시물 아이디: " + data[u"from"][u"id"].encode("utf-8").decode() + "\n")
    f.write("최종 업데이트 시간: " + data[u"updated_time"].encode("utf-8").decode() + "\n")
    f.write("게시물 링크: " + data[u"actions"][0][u"link"].encode("utf-8").decode() + "\n")

    if u"message" in data:  #게시물 내용이 있다면 추가
        f.write("게시물 내용: " + data[u"message"].encode("utf-8").decode() + "\n")

    if u"picture" in data:
        f.write("게시물 사진 이름: " + data[u"name"].encode("utf-8").decode() + "\n")
        f.write("사진 주소: " + data[u"picture"].encode("utf-8").decode() + "\n")

    if u"description" in data:
        f.write("사진 설명: " + data[u"description"].encode("utf-8").decode() + "\n")

f.write("==" * 30 + "\n")
f.close()