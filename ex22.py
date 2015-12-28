# -*- coding: utf-8 -*-

#Weak Reference
import sys
import weakref
class C:
	pass

#1. weakref.ref(o)
c = C()
c.a = 1
print "refcount - ", sys.getrefcount(c)  #
print

d = c  #
print "refcount - ", sys.getrefcount(c)
print

r = weakref.ref(c)  #
print "refcount - ", sys.getrefcount(c)
print


print r  #weakref object
print r()  #weakref object return

print c
print r().a  #

del c  #object remove
del d
print r()  #
#print r().a  #error

#
d = {'one': 1, 'two': 2}
#wd = weakref.ref(d)  #error

#2. weakref.proxy(o)
c = C()
c.a = 2
print "refcount - ", sys.getrefcount(c)  #
p = weakref.proxy(c)  #
print "refcount - ", sys.getrefcount(c)
print
print p
print c
print p.a

c = C()  #
r = weakref.ref(c)  #
p = weakref.proxy(c)  #
print weakref.getweakrefcount(c)  #
print weakref.getweakrefs(c)  #

#weak dictionary
c = C()
c.a = 4
d = weakref.WeakValueDictionary()  #
print d

d[1] = c  #
print d.items()  #
print d[1].a  #

del c  #
print d.items()  #

c = C()
c.a = 4
d = {}  #
print d

d[1] = c  #
print d.items()  #
print d[1].a  #

del c  #
print d.items()  #


#iterator
I = iter([1, 2, 3])
print I

print I.next()
print I.next()
print I.next()
#print I.next()  #error -> StopIteration

#list for~in
def f(x):
	print x + 1

for x in [1, 2, 3]:
	f(x)

#list iterator
t = iter([1, 2, 3])
while 1:
	try:
		x = t.next()
	except StopIteration:
		break
	f(x)

t = iter([1, 2, 3])
for x in t:
	f(x)

for x in iter([1, 2, 3]):
	f(x)

for x in iter((1, 2, 3)):
	f(x)

#class iterator
class Seq:
	def __init__(self, fname):
		self.file = open(fname)
	#def __getitem(self, n):
	#	if n == 10:
	#		raise StopIteration
	#	return n
	def __iter__(self):  #iter() matching
		return self
	def next(self):
		line = self.file.readline()  #
		if not line:
			raise StopIteration  #
		return line  #

s = Seq('removeme.txt')  #
for line in s:  #
	print line,

print

print Seq('removeme.txt')

print list(Seq('removeme.txt'))  #
print tuple(Seq('removeme.txt'))  #


#dictionary iterator
d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
for key in d:  #
	print key, d[key]

for key in iter(d):
	print key, d[key]

for key in d.iterkeys():  #key iterator
	print key

for value in d.itervalues():  #value iterator
	print value

keyset = d.iterkeys()
print keyset.next()  #
for key in keyset:  #
	print key,

for key, value in d.iteritems():  #key, value iterator
	print key, value

#file iterator
f = open('removeme.txt')
print "f.next()", f.next()
for line in f:
	print line,


#generator
def f(a, b):
	c = a * b
	d = a + b
	return c, d

def generate_ints(N):
	for i in range(N):
		yield i

gen = generate_ints(3)  #
print gen
print gen.next()  #
print gen.next()  #
print gen.next()  #
#print gen.next()  #error

for i in generate_ints(5):
	print i,


#list comprehension
print
print [k for k in range(100) if k % 5 == 0]

a = (k for k in range(100) if k % 5 == 0)  #generator
print a
print a.next()
print a.next()
print a.next()
for i in a:
	print i,

print
print sum((k for k in range(100) if k % 5 == 0))

def fibonacci(a = 1, b = 1):
	while 1:
		yield a
		a, b = b, a + b

for k in fibonacci():  #
	if k > 100:
		break
	print k,

#iterator
class Odds:
	def __init__(self, limit = None):  #
		self.data = -1  #
		self.limit = limit  #
	def __iter__(self):  #
		return self
	def next(self):  #
		self.data += 2
		if self.limit and self.limit <= self.data:
			raise StopIteration
		return self.data

for k in Odds(20):
	print k,
print
print list(Odds(20))  #

#generator
def odds(limit = None):
	k = 1
	while not limit or limit >= k:
		yield k
		k += 2

for k in odds(20):
	print k,
print
print list(odds(20))  #

#getOddSquare()함수 호출과 함께 인자에 값을 주면 해당 값보다 작은 홀수들에 대해
#제곱값을 반복적으로 출력
#for k in getOddSquare(10):
#print k,
#1 9 25 49 81 121 169 225 289 361

def getOddSquare(limit):
	n = 1
	while n <= limit:
		yield n * n
		n += 2

for k in getOddSquare(10):
	print k,
