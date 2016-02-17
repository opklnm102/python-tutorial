# -*- coding: utf-8 -*-

#function: 여러 개의 Statement들을 하나로 묶은 단위
#장점
#	반복적인 수행이 가능
#	코드를 논리적으로 이해하는데 도움
#	코드의 일정부분을 별도의 논리적 개념으로 독립화

#function define
#함수 이름 자체는 함수 객체의 레퍼런스를 지닌다.
#함수는 객체
def add(a, b):
	return a + b

print add(1, 2)
f = add  #레퍼런스를 다른 변수에 할당해 호출 가능
print f(4, 5)
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

#함수의 몸체에는 최소 1개 이상의 statement가 존재
#	아무런 내용이 없는 몸체를 지닌 함수를 만들 때는 pass키워드를 적는다.
def simpleFunction():  #empty function
	pass  #아무것도 수행하지 않고 지나가겠다는 의미

simpleFunction()

def addmember(members, newmember):
	if newmember not in members:  #기존 멤버가 아니면
		members.append(newmember)  #추가

members = ['hwang', 'lee', 'park']

addmember(members, 'jo')

addmember(members, 'lee')

print members

#함수 인수 전달방법
#	기본적으로 call by value.
#	하지만 변수에 저장된 값이 reference이므로 실제로는 call by reference로 실행
#인자에 Immutable객체인 숫자값 전달
#	함수 내에서 다른 숫자값으로 치환 -> 의미없는 인자 전달
#함수의 레퍼런스와 실행문의 레퍼런스가 따로
def f1(b):
	print b
	b = 100
	print b

a = 200  #a는 200의 레퍼런스값을 가진다.
f1(a)  #호출시 레퍼런스가 b에 복사
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

#인자에 Mmutable객체인 리스트 전달 및 내용 수정
#	전형적인 인자 전달 및 활용
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
	return  #인수 없이 리턴하면 None객체 리턴

print nothing()

def print_menu():
	print '1. Snack'
	print '2. Snake'
	print '3. Snick'

a = print_menu()  #return문이 없는 함수라도 실제로는 None객체 리턴
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
#모든 객체는 동적으로(실행시간에) 타입이 결정
#함수 호출시에 객체 타입에 맞게 실행됨
def add(a, b):
	return a + b

c = add(1, 3.4)
d = add('dynamic', 'typing')
e = add(['list'], ['and', 'list'])
print c
print d
print e

#function parameter
#1. default parameter: 인수를 넘겨주지 않아도 기본적으로 가지는 값
# default paremeter는 맨 뒤에 와야한다.
def incr(a, step=1):
	return a + step

b = 1
b = incr(b)  # 1 increment
print b

b = incr(b, 10)  #10 increment
print b

#여러개의 기본 인수 정의 가능
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
#함수 정의시 *var형식의 인수로 가변 인수를 선언
#호출시 일반 인수에 할당되는 값을 제외한 나머지 값들을 지닌 튜플객체 생성
def varg(a, *arg):  #*arg -> tuple type
	print a, arg
	print arg[0], arg[1]

varg(2,3,4,5,6)

#C language printf: 가변인수를 사용
def printf(format, *args):
	print format % args

printf("I've spent %d days and %d night to do this %d", 6, 5, 100)

#tuple, dictionary parameter
#함수 정의시 * 사용: 가변인수
#함수 호출시 * 사용: 튜플 전체 호출 가능
#함수 호출시 ** 사용: 사전 전체 호출 가능
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
