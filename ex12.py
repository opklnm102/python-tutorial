# -*- coding: utf-8 -*-

#Dictionary
#집합적 자료형
#자료의 순서를 정하지 않는 Mapping형
#	key를 이용하여 value에 접근
#	시퀀스 자료형이 아님
#key와 value의 mapping 1개를 item이라고 부름
#value를 저장할 시에 key를 사용
#	key가 없다면 새로운 key와 value의 아이템이 생성
#	key가 이미 존재한다면 그 key에 해당하는 값이 변경
#사전을 출력하면 각 아이템들이 임의의 순서로 출력
#새로운 아이템이 들어오면 key에 따라 순서가 달라진다.
#내부적으로 key 내용에 대해 Hash기법 사용
#	검색속도가 매우 빠름
#	[참고]: http://www.laurentluce.com/posts/python-dictionary-implementation/
#key와 value 매핑에 대한 item을 삭제할 때는 del(key) 사용
#key는 Immmutable. 문자열, 숫자, 튜플 가능
#value는 임의의 객체
print 'Dictionary'
member = {'basketball': 5, 'soccer': 11, 'baseball': 9}
print member['baseball']  #dictionary serarch

member['volleyball'] = 7  #item add
print member

member['volleyball'] = 6  #item modify
print member
print len(member)

del member['basketball']  #item delete
print member

d = {}
d['str'] = 'abc'
d[1] = 4
d[(1, 2, 3)] = 'tuple'
# d[[1, 2]] = 'list' # Type error -> unhashable type
# d[{1: 10}] = 'dictionary'
print d

def add(a, b):
	return a + b

def sub(a, b):
	return a - b

action = {0: add, 1: sub}  #함수의 이름을 사전의 value로
print action[0](4, 5)
print action[1](4, 5)
print
action2 = {add: 1, sub: 2}  #함수의 이름을 사전의 key로
print action2[add]

#dict()
d = dict()  #사전 생성  
print type(d)
print

print dict(one=1, two=2)  #{'one': 1, 'two': 2}
print dict([('one', 1), ('two', 2)])  #{'one': 1, 'two': 2}
print dict({'one': 1, 'two': 2})  #{'one': 1, 'two': 2} -> 노의미

keys = ['one', 'two', 'three']
values = (1, 2, 3)
print zip(keys, values)  #zip(): 두개의 자료를 순서대로 쌍으로 묶은 튜플의 리스트 반환
print dict(zip(keys, values))

#Dictionary methods
print 'Dictionary methods'
phone = {'jack': 946512, 'jin': 1111, 'joseph': 6584321}

print phone.keys()  #key들의 리스트 반환
print phone.values()  #value들의 리스트 반환
print phone.items()  #(key, value)의 리스트 반환
print
print 'jack' in phone  #key의 포함 여부
print 'lee' in phone
print 1111 in phone
print 1111 in phone.values()

#copy()
p = phone  #dictionary reference copy, dictionary 객체 공유

phone['jack'] = 1234  #phone을 변경하면
print phone
print p  #p도 함께 변경된다.
print

ph = phone.copy()  #dictionary copy, dictionary 객체 별도
phone['jack'] = 1111  #phone을 바꿔도
print phone
print ph  #ph는 바뀌지 않는다.

#copy() -> shallow copy(o), deep copy(x)
#shallow copy: 복사하려는 리스트 안 원소까지 복사X 
#deep copy: 복사하려는 리스트 안 원소까지 복사
phone = {'a': [1, 2, 3], 'b': 4}
phone2 = phone.copy()
print phone
print phone2
print

phone['b'] = 100
print phone
print phone2
print

phone['a'][0] = 100
print phone
print phone2

#get('key') = value
print
ph = {'jack': 9465215, 'jin': 1111, 'joseph': 6584321}

print ph.get('jack')
print ph.get('gslee')  #no key = None
print ph['jack']
# print ph['gslee'] #no key = error

print ph.get('gslee', 5284)  #get(key, default value)
print ph
print 

print ph.popitem()  #임의의 아이템을 꺼낸다.
print ph
print

print ph.pop('jack')  #key를 통해 해당 아이템을 지정하여 꺼낸다.
print ph

phone = {'jack': 946512, 'jin': 1111, 'joseph': 6584321}
ph = {'kim': 9465215, 'lee': 1111}
phone.update(ph)  #dictionary의 내용에 ph추가
print phone
print
phone.clear()  #dictionary의 모든 입력을 없앤다.
print phone

#loop
print 'Loop'
D = {'a': 1, 'b': 2, 'c':3}
#사전의 모든 key를 순차적으로 참조
for key in D.keys():  #key return
	print key, D[key]

print
D = {'a': 1, 'b': 2, 'c':3}
#사전 자체를 for에 활용하면 key에 대한 루프 실행
for key in D:
	print key, D[key]

print
D = {'a': 1, 'b': 2, 'c': 3}
for key, value in D.items():  #tuple로 된 list return
	print key, value

print
D = {'a': 1, 'b': 2, 'c': 3}
#key, value 동시 참조
for value in D.values():  #value가 list로 return
	print value

#사전에 입력된 아이템들은 일정한 순서X
#key에 대한 정렬은 아이템들을 리스트로 뽑은 다음 해당 리스트에 있는 sort()활용
print
D = {'a': 1, 'b': 2, 'c': 3}
items = D.items()  #tuple로 된 list return
print items
print

items.sort()  #tuple의 첫번째 값을 기준으로 정렬
print items
print

for k, v in items:
	print k, v
print

#dictionary d = {'aaa': 1, 'eee':5, 'bbb':2, 'ddd': 4, 'ccc': 3}에 존재하는
#값들(정수값)의 오름차순 기준으로  dictionary에 있는 각 아이템들을 정렬하여
#리스트 형태로 출력
def f(item):
	return item[1]

d = {'aaa': 1, 'eee':5, 'bbb':2, 'ddd': 4, 'ccc': 3}
items = d.items()
items.sort(key = f)
print items
