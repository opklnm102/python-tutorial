# -*- coding: utf-8 -*-

g = 10
h = 5

def f(x):
	h = x + 10  #h, x(local)
	b = h + x + g  #b, x, h(local), g(global)
	return b

print f(h)  #f(5)
print h  #global 
print

#
h = 5

def f(x):
	global h  #global variable use
	h = x + 10
	return h

print f(10)
print h

#scope error
g = 10

def f():
	global g  #error resolve1 -> global keyword
	#g = 20  #error resolve2 -> local variable
	x = g  #g(global)
	g = 20  #g(local)
	return x

print f()

#get name space
l = []
print dir(l)

#Nested Scopes
x = 2
def f():
	x = 1
	def g():
		print x
	g()

f()

#module definition
import mymath

print dir(mymath)
print mymath.mypi
print mymath.add(1, 10)
print mymath.area(10)

import string
print dir(string)

#name space
#1. module
string.a = 1  #string모듈 밖에서 새로운 변수를 정의하여 삽입
print string.a

#2. class, object
class C:
	a = 2
	pass

c = C()  #constructor call
c.a = 1  #instance inner variable
print c.a  ##instance variable
print c.__class__.a  #class variable
print C.a  #class variable

#3. method
#method 안에서 선언된 변수는 밖에서 조작 불가
x = 10
def f():
	a = 1
	b = 2
f.c = 1
print f.c
#print f.a  #error

#module search path
#1. in memory -> import
import string

#2. current directory

#3. PYTHON PATH

#code내에서 모듈 검색 경로 확인
import sys
print sys.path

#code내에서 모듈 검색 경로 추가
sys.path.append('~/Dev')
print sys.path
