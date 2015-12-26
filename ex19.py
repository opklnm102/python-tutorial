# -*- coding: utf-8 -*-

#class
class S1:  #header
	a = 1  #body

print S1.a
print

S1.b = 2  #클래스 이름 공간에 새로운 이름 생성
print S1.b
print

print dir(S1)  #S1에 포함된 이름들을 리스트로 반환
del S1.b  #이름 공간 S1에서 b삭제
print dir(S1)

x = S1()  #x는S1의 클래스 인스턴스, S1() -> 생성자 호출 
print x.a

x.a = 10  #클래스 인스턴스 x의 이름 공간에 이름 생성
print x.a

print S1.a  #클래스 이름공간과 클래스 인스턴스의 이름 공간은 다르다. 

y = S1()

y.a = 300

print y.a
print x.a
print S1.a


class Simple():
	pass

s1 = Simple()
s2 = Simple()

s1.stack = []  #
s1.stack.append(1)  #
s1.stack.append(2)
s1.stack.append(3)

print s1.stack
print s1.stack.pop()
print s1.stack.pop()
print
print s1.stack  #
#print s2.stack  #s2 -> error

del s1.stack  #

#class method
class MyClass:
	def set(self, v):
		self.value = v
	def get(self):
		return self.value

c = MyClass()  #
c.set('egg')  #
print c.get()  #
print c.value  #

c2 = MyClass()
MyClass.set(c2, 'egg')
print MyClass.get(c2)
print c2.value

class Simple:	
	pass

c = MyClass()
s1 = Simple()
#MyClass.set(s1, 'egg')  #자신의 레퍼런스만 가질 수 있다. -> error

#클래스 내부에서의 메소드 호출
class MyClass:
	def set(self, v):
		self.value = v
	def incr(self):
		self.set(self.value + 1)  #
	def get(self):
		return self.value

c = MyClass()
c.set(1)
print c.get()
c.incr()
print c.get()


#
def set(i):
	print 'set function - ', i

class MyClass:
	def set(self, v):
		self.value = v
	def incr(self):
		set(self.value + 1)  #
	def get(self):
		return self.value

c = MyClass()
c.set(1)
print c.get()
c.incr()
print c.get()

#static method
class D:
	@staticmethod
	def spam(x, y):
		print 'static method', x, y

D.spam(1, 2)  #인스턴스 객체없이 클래스에서 직접 호출
print
d = D()
d.spam(1, 2)  #인스턴스 객체를 통해서도 호출 가능(비추천)

#class method
class C:
	@classmethod
	def spam(cls , y):
		print cls, '->', y

print C

C.spam(5)  #첫번째 인수로 C가 잠재적으로 전달
c = C()
c.spam(5)  #인스턴스를 통해서도 호출 가능(비추천)

#subclass

class D(C):  #상속
	pass

D.spam(3)  #첫번째 인수로 서브클래스가 전달

d = D()
d.spam(3)  #인스턴스를 통해서도 호출 가능(비추천)

#class member vs instance member
class Var:
	c_mem = 100  #class member
	def f(self):
		self.i_mem = 200  #instance member
	def g(self):
		print self.i_mem
		print self.c_mem

print Var.c_mem

v1 = Var()
print v1.c_mem
v1.f()
print v1.i_mem

print 
v2 = Var()
#print v2.i_mem  #인스턴스 v2에는 아직 i_mem이 없다. -> error

#instanceName.memberName으로 멤버를 참조할 때 순서
#1. instance member
#2. instance member가 없다면 class member
print v1.c_mem  #인스턴스 v1를 통해 클래스 맴버 참조
print v2.c_mem  #인스턴스 v2를 통해 클래스 맴버 참조

print
v1.c_mem = 50  #인스턴스 이름 공간에 c_mem생성
print v1.c_mem  #인스턴스 v1를 통해 인스턴스 맴버 참조
print v2.c_mem  #인스턴스 v2를 통해 클래스 맴버 참조

print Var.c_mem  #클래스 맴버 참조

#constructor, destructor
from time import ctime, sleep

class Life:
	def __init__(self):  #constructor
		self.birth = ctime()  #current time
		print 'Birthday', self.birth 
	def __del__(self):  #destructor
		print 'Deathday', ctime()

def test():
	mylife = Life()
	print 'Sleeping for 3 sec'
	sleep(3)  #3초간 sleep(block)상태에 있음(CPU 점유 못함)

test()

class Integer:
	def __init__(self, i):
		self.i = i
	def __str__(self):
		return "---" + str(self.i) + "---"

i = Integer(10)
print i  # ==str(i)
print str(i)

#k = MyInteger(10)
#print k
#10
#k = k.increment(5)
#print k
#15
#k = k.sub(10)
#print k
#5
#가 정상적으로 실행되도록 class를 정의

class MyInteger:
	def __init__(self, n):
		self.n = n
	def __str__(self):
		return str(self.n)
	def increment(self, n):
		self.n = self.n + n
		return self
	def sub(self, n):
		self.n = self.n - n
		return self	
	
k = MyInteger(10)
print k
k = k.increment(5)
print k
k = k.sub(10)
print k

