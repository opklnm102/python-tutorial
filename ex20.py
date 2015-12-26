# -*- coding: utf-8 -*-

#Operator Overloading
#1. 수치 연산자 중복 
class Integer:
	def __init__(self, n):
		self.n = n
	def __str__(self):
		return str(self.n)
	def __add__(self, other):
		#return self.n + other  #reutrn int
		self.n = self.n + other
		return self  #return instance

i = Integer(10)
print i
print str(i)

print
i = i + 10
print i

print
i += 10
print i
print type(i)

class MyString:
	def __init__(self, str):
		self.str = str

	def __div__(self, sep):  #나누기 연산자 '/'가 사용되었을 때 호출
		return self.str.split(sep)  #문자열 self.str을 sep를 기준으로 분리

	__rdiv__ = __div__

	def __neg__(self):  # -(단항)
		t = list(self.str)
		t.reverse()
		return ''.join(t)

	__invert__ = __neg__  # ~


m = MyString("abcd_abcd_abcd")
print m / "_"  #__div__ call
print m / "_a"

print 
print m.__div__("_")

print
print "_" / m  #__rdiv__ call
print "_a" / m

print -m  #__neg__ call
print ~m  #__invert__ call

class MyCmp:
	def __cmp__(self, y):
		return 1 - y

c = MyCmp()
print c > 1  #c.__cmp__(1) call, 반환값이 양수여야 True 
print c < 1  #c.__cmp__(1) call, 반환값이 음수여야 True
print c == 1  #c.__cmp__(1) call, 반환값이 0 이여야 True

class MyCmp2:
	def __lt__(self, y):
		return 1 < y

m = MyCmp2()
print m < 10  #m.__lt__(10) call
print m < 2
print m < 1

class MyCmp3:
	def __eq__(self, y):
		return 1 == y

m = MyCmp3()
print m == 10  #m.__eq__(10) call
m1 = MyCmp3()
print m == 1

class MyCmp4():
	def __init__(self, value):
		self.value = value
	def __cmp__(self, other):
		if self.value == other:
			return 0

m2 = MyCmp4(10)
print m2 == 10

#2. sequence, mapping 연산자 중복
class Square:
	def __init__(self, end):
		self.end = end
	def __len__(self):
		return self.end
	def __getitem__(self, k):
		if k < 0 or self.end <= k:
			raise IndexError, k
		return k * k

s1 = Square(10)
print len(s1)  #s1.__len__()
print s1[1]  #s1.__getitem__(1)
print s1[4]
#print s1[20]

 #s1[0], s1[1], s1[2]...
for x in s1:  #s1.__getitem()__ call, error발생 시 for ~ in멈춤
	print x,

print
print list(s1)  #각 원소의 __getitem()__ call
print tuple(s1)  #각 원소의 __getitem()__ call

class MyDict:
	def __init__(self, d = None):
		if d == None:
			d = {}
		self.d = d
	def __getitem__(self, key):
		return self.d[key]
	def __setitem__(self, key, value):
		self.d[key] = value
	def __len__(self):
		return len(self.d)
	def keys(self):
		return self.d.keys()
	def values(self):
		return self.d.values()
	def items(self):
		return self.d.items()

m = MyDict()  #__init__ call
m['day'] = 'light'  #__setitem__ call
m['night'] = 'darkness'  #__setitem__ call
print m
print m['day']  #__getitem__ call
print m['night']  #__getitem__ call
print len(m)  #__len__ call

m = MyDict({'one': 1, 'two': 2, 'three': 3})
print m.keys()
print m.values()
print m.items()

#3. string transfer
#1) __repr__
#2) __str__

class StringRepr:
	def __repr__(self):
		return 'repr called'
	def __str__(self):
		return 'str called'

s = StringRepr()
print s  #__str__ call
print str(s)  #__str__ call
print repr(s)  #__repr__ call
print 's'  #__repr__ call

#__str__(x) -> __repr__ call
class StringRepr:
	def __repr__(self):
		return 'repr called'

s = StringRepr()
print s
print repr(s)
print str(s)
print 's'

#__repr__(x) -> __str__ not call
class StringRepr:
	def __str__(self):
		return 'str called'

s = StringRepr()
print s
print str(s)
print repr(s)
print 's'

#호출 가능한 클래스 인스턴스 만들기
class Accumulator:
	def __init__(self):
		self.sum = 0
	def __call__(self, *args):
		self.sum += sum(args)
		return self.sum

acc = Accumulator()
print acc(1, 2, 3, 4, 5)
print acc(6)
print acc(7, 8, 9)
print acc.sum	

#호출 가능 객체인지 알아보기
def check(func):
	if callable(func):
		print 'callable'
	else:
		print 'not callable'

class B:
	def func(self, v):
		return v

class A:
	def __call__(self, v):
		return v

a = A()
b = B()
check(a)
check(b)
print
print callable(a)
print callable(b)
print callable(A)  #모든 클래스는 callable하다.(생성자가 있어서)
print callable(B)
