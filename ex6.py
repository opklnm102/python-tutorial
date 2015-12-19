# -*- coding: utf-8 -*-

a = 1
b = 2

if a < 10:
	c = 1
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

#for
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

#enumerate()
print
l = ['cat', 'dog', 'bird', 'pig']
for k, animal in enumerate(l):
	print k, animal

print
d = {'c':'cat', 'd':'dog', 'b':'bird', 'p':'pig'}
for k, key in enumerate(d):
	print k, key, d[key]

#break
print
for x in range(10):
	if x > 3:
		break
	print x
print 'done'

#continue
print
for x in range(10):
	if x < 8:
		continue
	print x
print 'done'

for x in range(10):
	print x,
else:
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
def add(a, b):
	return a + b

print add(3,4)

print add([1,2,3], [4,5,6])

c = add(10, 30)
print c

f = add
print f(4,5)

print f
print f is add

def simple():
	pass

print simple()

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

print minus(a = 12, b = 20)
print minus(b = 20, a = 12)

def incr(x, y = 1):
	return x + y

print incr(5)

print incr(5,10)


def calc(x, y):
	return x + y, x - y, x * y, x / y

print calc(10, 2)

def add(a, b):
	return a + b

c = add(1, 3.4)
d = add('dynamic', 'typing')
e = add(['list'], ['and', 'list'])

print c
print d
print e

def sum(N):
	if N == 1:
		return 1
	return N + sum(N-1)

print sum(10)

#구구단을 2단~19단까지 출력
for x in range(2, 20):
	for y in range(1, 10):
		print x, '*', y, '=', x*y