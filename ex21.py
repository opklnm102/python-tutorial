# -*- coding: utf-8 -*-

#상속
class Person:
	def __init__(self, name, phone=None):
		self.name = name
		self.phone = phone
	def __str__(self):
		return '<Person %s %s>' % (self.name, self.phone)

class Employee(Person):  #괄호안에 쓰여진 클래스는 슈퍼클래스
	def __init__(self, name, phone, position, salary):  #overriding
		Person.__init__(self, name, phone)  #Person클래스의 생성자 호출
		self.position = position
		self.salary = salary

p1 = Person('dong', 1498)
print p1.name
print p1

print

m1 = Employee('kim', 5434, 'publisher', 200)
m2 = Employee('hee', 3341, 'team leader', 300)
print m1.name, m1.position  #super class, sub class member print
print m1
print m2.name, m2.position
print m2

#constructor call
#1. 
class Super:
	def __init__(self):
		print 'Super init called'

class Sub(Super):
	def __init__(self):
		print 'Sub init called'

s = Sub()

#2. 
class Sub(Super):
	def __init__(self):
		Super.__init__(self)
		print 'Sub init called'

s = Sub()

#3.
class Sub(Super):
	pass

s = Sub()

#method override
class Person:
	def __init__(self, name, phone=None):
		self.name = name
		self.phone = phone
	def __str__(self):
		return '<Person %s %s>' % (self.name, self.phone)

class Employee(Person):  #괄호안에 쓰여진 클래스는 슈퍼클래스
	def __init__(self, name, phone, position, salary):  #overriding
		Person.__init__(self, name, phone)  #Person클래스의 생성자 호출
		self.position = position
		self.salary = salary
	def __str__(self):  #overriding
		return '<Employee %s %s %s %s>' % (self.name, self.phone, self.position, self.salary)

p1 = Person('dong', 1498)
m1 = Employee('kim', 5434, 'publisher', 200)

print p1
print m1

#polymorphism
class Animal:
	def cry(self):
		print '...'

class Dog(Animal):
	def cry(self):
		print "dog dog"

class Duck(Animal):
	def cry(self):
		print "duck duck"

class Fish(Animal):
	pass

for each in (Dog(), Duck(), Fish()):
	each.cry()

#내장 자료형과 클래스의 통일
a = list()  # == a = []
print a
print dir(a)

class MyList(list):
	def __sub__(self, other):  # '-' overloading
		for x in other:
			if x in self:
				self.remove(x)
		return self

L = MyList([1, 2, 3, 'spam', 4, 5])
print L
print

L = L - ['spam', 4]
print L

L.append('aaa')
print L

#1. Stack
print 'Stack'
class Stack(list):
	push = list.append

s = Stack()

s.push(4)
s.push(5)
print s
print

s = Stack([1, 2, 3])
s.push(4)
s.push(5)
print s
print

print s.pop()  #super class pop() called
print s.pop()
print s

#2. Queue
print 'Queue'
class Queue(list):
	enqueue = list.append
	def dequeue(self):
		return self.pop(0)

q = Queue()
q.enqueue(1)  #data input
q.enqueue(2)
print q

print q.dequeue()  #data output
print q.dequeue()

#
a = dict()  # == a = {}
a = dict({'a': 1, 'b': 2})
print a
print dir(a)

class MyDict(dict):
	def keys(self):  #overriding
		K = dict.keys(self)  #unbound method call
		#K = self.keys() -> recursive call
		K.sort()
		return K

d = MyDict({'one': 1, 'two': 2, 'three': 3})
print d.keys()
print

d2 = {'one': 1, 'two': 2, 'three': 3}
print d2.keys()

#class information get
#객체가 어던 클래스에 속해 있는지 확인
#객체의 자료형 비교 방법1. (전통적, 비추) 
import types

print type(123) == types.IntType
print type(123) == type(0)

#객체의 자료형 비교 방법2. (새로운)
print isinstance(123, int)
print int

class A:
	pass

class B:
	def f(self):
		pass

class C(B):
	pass

def check(obj):
	print obj, '=>',
	if isinstance(obj, A):
		print 'A',
	if isinstance(obj, B):
		print 'B',
	if isinstance(obj, C):
		print 'C',
	print

a = A()
b = B()
c = C()

check(a)
check(b)
check(c)

#클래스 간의 상속 관계 확인
def check(obj):
	print obj, '=>',
	if issubclass(obj, A):
		print 'A',
	if issubclass(obj, B):
		print 'B',
	if issubclass(obj, C):
		print 'C',
	print

check(A)
check(B)
check(C)
