# -*- coding: utf-8 -*-

a = 1
b = 2

if a < 10:  #실행하는 함수문의 헤더
	c = 1  #밑 라인은 함수문의 몸체 역할 수행
	d = 10

	if b > 10:
		f = 10
	g = 10
	t = 200
x = 10

#if, elif, else
score = 90
if score >= 90:
	print 'Congratualations!!!'

a = 10
if a > 5:
	print 'Big'
else:
	print 'Small'

n = -2
if n > 0:
	print 'Positive'
elif n < 0:
	print 'Negative'
else:
	print 'Zero'

order  = 'spagetti'
if order == 'spam':
	price = 500
elif order == 'ham':
	price = 700
elif order == 'egg':
	price = 300
elif order == 'spagetti':
	price = 900

print price

#dictionary을 활용, 위와 똑같은 문제
order  = 'spagetti'
menu = {'spam':500, 'ham':700, 'egg':300, 'spagetti':900}
price = menu[order]
print price

#for문 형식
#for <타겟> in <컨테이너 객체>:  #컨테이너 객체에서 원소를 꺼내 타겟에 삽입
#	statements
#else:
#	statements
print
a = ['cat', 'cow', 'tiger']
for x in a:
	print len(x), x

print
for x in [1,2,3]:
	print x

print 
print range(10)

for x in range(10):
	print x

print
sum = 0
for x in range(1, 11):
	sum = sum + x
print 'sum =' ,sum

print
prod = 1
for x in range(1,11):
	prod = prod * x
print prod

#enumerate(): 컨테이너 객체가 지닌 각 요소, 인덱스 함께 반환
print
l = ['cat', 'dog', 'bird', 'pig']
for k, animal in enumerate(l):
	print k, animal

print
d = {'c':'cat', 'd':'dog', 'b':'bird', 'p':'pig'}
for k, key in enumerate(d):
	print k, key, d[key]

#break: 루프문을 빠져나간다.
print
for x in range(10):
	if x > 3:
		break
	print x
print 'done'

#continue: 루프블록 내의 continue이후 부분은 수행하지 않고 루프의 시작부분으로 이동
print
for x in range(10):
	if x < 8:
		continue
	print x
print 'done'

for x in range(10):
	print x,
else:  #break에 의한 중단 없이 정상적으로 모두 수행되면 else블록이 수행
	print 'else block'

print 'done'

for x in range(10):
	break
	print x,
else:
	print 'else block'
print 'done'

for x in range(2,4):
	for y in range(2,10):
		print x, '*', y, '=', x*y
	print

#while
print
count = 1
while count < 11:
	print count
	count = count + 1

print
sum = 0
a = 0
while a < 10:
	a = a + 1
	sum = sum + a
print sum

x = 0
while x < 10:
	print x,
	x = x + 1
else:
	print 'else block'
print 'done'


#function
#장점: 반복적인 코드를 없애주어 코드의 길이를 짧게, 유지보수를 쉽게 만든다.
def add(a, b):
	return a + b

print add(3,4)

print add([1,2,3], [4,5,6])

c = add(10, 30)
print c

#함수 이름에 저장된 레퍼런스를 다른 변수에 할당하여 그변수를 이용해 호출 가능
f = add
print f(4,5)

print f  #<f 식별자의 형, 실제 식별자 이름, 객체가 놓여져 있는 메모리 위치>
print f is add

#최소 1개 이상의 statement가 존재해야함.
def simple():
	pass  #아무런 내용이 없는 몸체를 지닌 함수

print simple()  #None객체 리턴

def myabs(x):
	if x < 0:
		x = -x
	return x

print myabs(4)

def addabs(a, b):
	c = add(a, b)
	return myabs(c)

print addabs(-5, -7)

def minus(a, b):
	return a - b

#인자의 이름과 함께 인자 값을 넘겨줄 수 있다.
#순서에 상관없어진다.
print minus(a = 12, b = 20)
print minus(b = 20, a = 12)

#인자의 디폴트 값을 지정할 수 있다.
def incr(x, y = 1):
	return x + y

print incr(5)

print incr(5,10)

#2개 이상의 값을 동시에 반환할 수 있다. 튜플로
def calc(x, y):
	return x + y, x - y, x * y, x / y

print calc(10, 2)  #(12,8,20,5)

def add(a, b):
	return a + b

#모든 객체는 동적으로(실행시간에) 타입이 결정
c = add(1, 3.4)
d = add('dynamic', 'typing')
e = add(['list'], ['and', 'list'])

print c
print d
print e

#재귀(Recursive) 함수
def sum(N):
	if N == 1:
		return 1
	return N + sum(N-1)

print sum(10)

#구구단을 2단~19단까지 출력
for x in range(2, 20):
	for y in range(1, 10):
		print x, '*', y, '=', x*y

#2진수변환
decimal = 10
result = ""
while(decimal > 0):
	remainder = decimal % 2
	decimal = decimal / 2
	result = str(remainder) + result
print result

