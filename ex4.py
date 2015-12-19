# -*- coding: utf-8 -*-

#list
print '---------list---------'
L = [1,2,3]
print type(L)
print len(L)
print L[1]
print L[-1]
print L[1:3]
print L + L
print L * 3

l1 = [4,5,6]
print l1
l1[0] = 10
print l1

L = range(10)
print L
print L[::2]
print L[::-1]
print 4 in L

#tuple
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

#dictionary
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
print type(3)
print type(3.3)
print type('abc')
print type([])
print type(())
print type({})

a = 0
L = [1,2,3]
print type(a) == type(0)
print type(L) == type([])
print type(L[0])  == type(0)
print type(None)
a = None
print a
print type(a)

#id()
print
print '------------id()-------------'
a = 500
b = a
print id(a)
print id(b)
print
x = 1
y = 1
print id(x)
print id(y)

print
c = [1,2,3]
d = [1,2,3]
print c is d

a = 500
b = a
print a is b

x = 1
y = 1
print x is y

e = f = [4,5,6]
print e is f

c = [1,2,3]
d = [1,2,3]
print c == d

#'Hello','World'라는 2개의 단어들을 Key로 하는 Dictionary 자료형을 새롭게 정의한 후 각 Key에 대응되는 
#Value을 각 단어들의 길이로 저장하고, 마지막으로 해당 사전을 출력하는 프로그램
w1 = 'Hello'
w2 = 'World'
d = {}
d[w1] = len(w1)
d[w2] = len(w2)
print d


