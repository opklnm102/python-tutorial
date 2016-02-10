# -*- coding: utf-8 -*-

#list: 임의의 객체를 순차적으로 저장하는 집합적 자료형
print '---------list---------'
L = [1,2,3]
print type(L)  #타입
print len(L)  #길이
print L[1]  #인덱스1의 값
print L[-1]  #인덱스가 뒤에서 1번째인 값
print L[1:3]  #인덱스 1~3까지 슬라이싱
print L + L  #리스트2개를 합처 하나의 리스트로
print L * 3  #리스트를 숫자만큼 반복하여 하나의 리스트로

#리스트는 변경가능
l1 = [4,5,6]
print l1
l1[0] = 10
print l1

#range(k): 0부터 k-1까지의 숫자의 리스트를 반환
L = range(10)
print L
print L[::2]
print L[::-1]
print 4 in L  #L안에 4가 있다.

#tuple: 리스트와 유사하지만 값을 변경할 수 없음, 상수와 비슷한 속성
print
print '---------tuple---------'
t = (1,2,3)
print t
print len(t)
print t[0]
print t[-1]
print t[0:2]
print t[::2]
print t + t + t
print t * 3
print 3 in t

#dictionary: 키를 이용하여 값을 저장하는 자료구조, 활용빈도가 높다.
print
print '---------dictionary---------'
d = {'one':'hana','two':'dul','three':'set'}
print d['one']
d['four'] = 'net'  #새 항목의 삽입
print d
d['one'] = 1  #기존 항목의 값 변경
print d
print 'one' in d  #키에 대한 멤버쉽 테스트

print d.keys()  #키만 리스트로 추출
print d.values()  #값만 리스트로 추출
print d.items()  #키와 값의 튜플을 리스트로 반환

#type()
print
print '------------type()-------------'
print type(3)  #정수
print type(3.3)  #실수
print type('abc')  #문자열
print type([])  #리스트
print type(())  #튜플
print type({})  #사전

#자료형의 비교
a = 0
L = [1,2,3]
print type(a) == type(0)
print type(L) == type([])
print type(L[0])  == type(0)
print type(None)  #None객체, 아무 값도 없다(혹은 아니다)를 나타나는 객체
a = None
print a
print type(a)

#id(): 객체의 식별자를 반환
print
print '------------id()-------------'
a = 500
b = a  #서로 같은 식별자를 나타냄
print id(a)
print id(b)
print
#숫자를 따로 객체로 만들지 않는다.(이미존재)
#서로 같은 식별자를 나타냄
x = 1
y = 1
print id(x)
print id(y)

#is: 두 객체의 식별자가 동일한지 테스트
print
#내용이 같은 리스트라도 다른 객체
c = [1,2,3]
d = [1,2,3]
print c is d

#숫자는 이미 존재
a = 500
b = a
print a is b

x = 1
y = 1
print x is y

e = f = [4,5,6]
print e is f

#==: 두 객체의 값이 동일한지를 테스트
c = [1,2,3]
d = [1,2,3]
print c == d  #c와 d는 서로다른 객체를 가지지만 내용이 같으므로 True

#'Hello','World'라는 2개의 단어들을 Key로 하는 Dictionary 자료형을 새롭게 정의한 후 각 Key에 대응되는 
#Value을 각 단어들의 길이로 저장하고, 마지막으로 해당 사전을 출력하는 프로그램
w1 = 'Hello'
w2 = 'World'
d = {}
d[w1] = len(w1)
d[w2] = len(w2)
print d


