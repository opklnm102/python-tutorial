#facebook 특정 게시글에서 특정인이 쓴 댓글 찾기

import facebook
import os

obj = facebook.GraphAPI(access_token="EAACEdEose0cBAJTHaZBGaEJDM65HzzE8m0tgGw4Nz3Q7YdWjsEMIaUS2zWMSh7QmflVZBl4yhsFJs6Y03Acxa0YZB5bKVPezOfpKuLtNZAyWzL0itd3p9wWEu97JSaYDTD9KVZABMX6RtmkWZBIdEgByBGg1v1JweMa90yX0qYnQZDZD")
post_id = str(input("게시글 아디이를 입력하세요: "))
user_id = input("찾으실 유저의 이름을 입력하세요: ")

response = obj.get_connections(id=post_id, connection_name="comments", limit=25)
find = []
while response[u"data"]:
    #print(response[u"data"])  #확인
    for data in response[u"data"]:
        print(data)
        try:
            if user_id == data[u"from"][u"name"]:
                detail_data = {}
                detail_data["id"] = data[u"from"][u"id"]
                detail_data["name"] = data[u"from"][u"name"]
                detail_data["created_time"] = data[u"created_time"]
                detail_data["message"] = data[u"message"]
                find.append(detail_data)
        except UnicodeEncodeError as e:
            if user_id.decode("cp949") == data[u"from"][u"name"]:
                detail_data = {}
                detail_data["id"] = data[u"from"][u"id"]
                detail_data["name"] = data[u"from"][u"name"]
                detail_data["created_time"] = data[u"created_time"]
                detail_data["message"] = data[u"message"]
                find.append(detail_data)
    if u"paging" in response and u"after" in response[u"paging"][u"cursors"]:  #다음 페이지 이동
        after = response[u"paging"][u"cursors"][u"after"]
        response = obj.get_connections(id=post_id, connection_name="comments", limit=25,after=after)
    else:
        break

#print(find)  #확인

f = open(os.getcwd() + "/comments.txt", 'w')
for data in find:
    f.write("==" * 30 + '\n')
    f.write(data["created_time"].encode("utf-8").decode() + '\n')
    f.write(data["message"].encode("utf-8").decode() + '\n')
    f.write(data["id"].encode("utf-8").decode() + '\n')
    f.write(data["name"].encode("utf-8").decode() + '\n')
    f.write("==" * 30 + '\n')
f.close()






