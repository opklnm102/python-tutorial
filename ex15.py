# -*- coding: utf-8 -*-

#function
def add(a, b):
	return a + b

print add(1, 2)
print

def myabs(x):
	if x < 0:
		x = -x
	return x

print abs(-4)
print myabs(-4)
print

c = add(10, 30)
print c

f = add
print f(4, 5)

print f
print f is add

def simpleFunction():  #empty function
	pass

simpleFunction()

def addmember(members, newmember):
	if newmember not in members:
		members.append(newmember)  #add

members = ['hwang', 'lee', 'park']

addmember(members, 'jo')

addmember(members, 'lee')

print members

#
#형식은 call by value -> 내용은 call by reference
def f1(b):
	print b
	b = 100
	print b

a = 200
f1(a)
print a

def f2(b):
	b = "abc"
	#b[0] = 's'  #error
	print b[0]

a = "def"
f2(a)
print a

def f3(b):
	b = (1, 2, 3)
	#b[0] = 1000 -> error

a = (4, 5, 6)
f3(a)
print a

def f4(b):
	b[1] = 10

a = [4, 5, 6]
f4(a)
print a

def f5(b):
	b['a'] = 10

a = {'a': 1, 'b': 2}
f5(a)
print a

#return statement
#None return
def nothing():
	return

print nothing()

def print_menu():
	print '1. Snack'
	print '2. Snake'
	print '3. Snick'

a = print_menu()
print a

#single return
def myabs(x):
	if x > 0:
		return -x
	return x

print myabs(-10)

#multiple return
def swap(x, y):
	return y, x  #',' (=(y,x)) single tuple return

a = 10
b = 20
print a, b
print

a, b = swap(a, b)
print a, b
t = swap(a, b)
print t
print t[0], t[1]
print

def length_list(l):
	res = []
	for el in l:
		res.append(len(el))
	return res

l = ['python', 'pyson', 'pythong', 'pydon']
print length_list(l)
print [len(s) for s in l]

#dynamic typing
def add(a, b):
	return a + b

c = add(1, 3.4)
d = add('dynamic', 'typing')
e = add(['list'], ['and', 'list'])
print c
print d
print e

#function parameter
#1. default parameter
# default paremeter는 맨 뒤에 와야한다.
def incr(a, step=1):
	return a + step

b = 1
b = incr(b)  # 1 increment
print b

b = incr(b, 10)  #10 increment
print b

def incr(a, step=1, step2=10):
	return a + step + step2

print incr(10)

#2. keyword parameter
def area(height, width):
	return height * width

#순서가 아닌 이름으로 값이 전달
a = area(height='height string ' ,width=3)
print a

b = area(width=20, height=10)
print b

#keyword paremeter는 맨뒤에 위치
print area(20, width=5)
#print area(width=20, 5)  #error

#default + keyword parameter
def incr(a, step1=1, step2=10, step3=100):
	return a + step1 + step2 + step3

print incr(10, 2, step2=100)
#print incr(10, 2, step2=100, 200)  #error
print incr(10, 2, step2=100, step3=200)

#가변 인수 리스트
def varg(a, *arg):  #*arg -> tuple type
	print a, arg
	print arg[0], arg[1]

varg(2,3,4,5,6)

#C language printf
def printf(format, *args):
	print format % args

printf("I've spent %d days and %d night to do this %d", 6, 5, 100)

#tuple, dictionary parameter
def h(a, b, c):
	print a, b, c

args = (1, 2, 3)
h(args[0], args[1], args[2])
h(*args)

dargs = {'a': 1, 'b': 2, 'c': 3}  #인자의 이름과 동일한 키값을 가져야 한다.
h(**dargs)

#임의의 문자열로 이루어진 리스트를 받아서 각 문자열 마지막에 '!'를 덧붙인 새로운
#리스트를 반환하는 함수 myfunc(t)를 정의하고 테스트
def myfunc(t):
	res = []
	for el in t:
		res.append(el + '!')
	return res

l = ["Hello", "Python", "Programming", "Language"]
print myfunc(l)
