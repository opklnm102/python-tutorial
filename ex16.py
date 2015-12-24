# -*- coding: utf-8 -*-

#lambda function
f = lambda x: x + 1
print f(1)

g = lambda x, y: x + y
print g(1, 2)

incr = lambda x, inc = 1: x + inc
print incr(10)  #inc default parameter
print incr(10, 5)

vargs = lambda x, *args: args
print vargs(1, 2, 3, 4, 5)

#general function
def f1(x):
	return x*x + 3*x -10

def f2(x):
	return x*x*x

def g(func):
	return [func(x) for x in range(-10, 10)]

print g(f1)
print g(f2)

#lambda function
def g(func):
	return [func(x) for x in range(-10, 10)]

print g(lambda x: x*x + 3*x - 10)
print g(lambda x: x*x*x)



func = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]

def menu():
	print "0. add"
	print "1. sub"
	print "2. mul"
	print "3. div"
	print "4. quit"
	return input('Select menu: ')

while 1:
	sel = menu()
	if sel < 0 or sel > len(func):
		continue
	if sel == len(func):
		break
	x = input('First operand: ')
	y = input('Second operand: ')
	print 'Result = ', func[sel](x, y)

#map(function, seq)
def f(x):
	return x * x

X = [1, 2, 3, 4, 5]
Y = map(f, X)
print Y

#map() -> x
def f(x):
	return x * x

X = [1, 2, 3, 4, 5]
Y = []
for x in X:
	y = f(x)
	Y.append(y)
print Y

#map() + lambda -> recommend
X = [1, 2, 3, 4, 5]
print map(lambda x: x * x, X)

#
Y = map(lambda x: x*x + 4*x + 5, range(10))
print Y

#
y = map(lambda x: len(x), ["Hello", "Python", "Sing"])
print y

#filter(function, seq)
#filter() + lambda
print filter(lambda x: x > 2, [1, 2, 3, 34])

#filter() + lambda -> x
y = []
for x in [1, 2, 3, 34]:
	if x > 2:
		y.append(x)
print y

#
print filter(lambda x: x % 2, [1, 2, 3, 4, 5, 6])  #x % 2 = 1(True), = 0(False)

def f():
	x = 1
	print filter(lambda a: a > x, range(-5, 5))

f()

print filter(lambda x: x > 2, [1, 2, 3, 34])
print filter(lambda x: x > 2, (1, 2, 3, 34))
print filter(lambda x: x < 'a', 'abcABCdefDEF')  #ASCII Code compare

#reduce(function, seq[, inital]) -> parameter two
print reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])

print reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 100)

#1 ~ 10
#reduce() + lambda 
print reduce(lambda x, y: x + y * y, range(1, 11), 0)

#reduce() + lambda - > x
x = 0
for y in range(1, 11):
	x = x + y * y
print x

#string reverse -> lambda를 어떻게 작성하느냐에 따라 다채로운 결과가 나올 수 있다.
print reduce(lambda x, y: y + x, 'abcde')

#주어진 리스트 t=[1,2,3,4,5,6,7,8,9]에 대해 홀수만 필터링하여 총합을 구해라
#lambda, filter(), reduce() 사용
t = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_list = filter(lambda x: x % 2, t)
print reduce(lambda x, y: x + y, odd_list)

print reduce(lambda x, y: x + y, filter(lambda x: x % 2, t))

