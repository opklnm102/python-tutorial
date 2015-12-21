# -*- coding: utf-8 -*-

#Dictionary
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
d = dict()
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

print ph.popitem()
print ph
print

print ph.pop('jack')
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
for key in D.keys():  #key return
	print key, D[key]

print
D = {'a': 1, 'b': 2, 'c':3}
for key in D:
	print key, D[key]

print
D = {'a': 1, 'b': 2, 'c': 3}
for key, value in D.items():  #tuple로 된 list return
	print key, value

print
D = {'a': 1, 'b': 2, 'c': 3}
for value in D.values():  #value가 list로 return
	print value

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
