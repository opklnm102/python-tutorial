# -*- coding: utf-8 -*-

#class: 새로운 이름 공간을 지원하는 또 다른 단위
#클래스 정의 구문
class S1:  #header
	a = 1  #body

print S1.a
print
#인스턴스: 클래스로부터 만들어낸 객체
#모듈 vs 클래스 vs 인스턴스: 이름공간을 제공해주는 대표적인 단위
#	모듈: 파일 단위로 이름 공간을 구성
#	클래스: 클래스 영역 내에 이름공간을 구성
#	인스턴스: 인스턴스 영역 내에 이름공간을 구성

S1.b = 2  #클래스 이름 공간에 새로운 이름 생성
print S1.b
print

print dir(S1)  #S1에 포함된 이름들을 리스트로 반환
del S1.b  #이름 공간 S1에서 b삭제
print dir(S1)

#동적으로 인스턴스 외부에서 인스턴스 멤버를 추가할 수 있음
#	클래스와 독립적으로 각 인스턴스를 하나의 이름공간으로 취급
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
#클래스 내부에 메소드 선언 -def 키워드 사용
#일반 변수와 다른 점은 첫번째 인수로 self사용(관례적)
#	self: 인스턴스 객체 자신의 레퍼런스를 지니고 있음
#	각 인스턴스들은 self를 이용하여 자신의 이름공간에 접근
class MyClass:
	def set(self, v):
		self.value = v
	def get(self):
		return self.value

#인스턴스 객체를 통하여 메소드를 호출할 때 self인자는 없다고 생각
c = MyClass()  #인스턴스 생성
c.set('egg')  #set() 호출
print c.get()  #get() 호출
print c.value  #인스턴스 변수에 직접 접근

#아래코드는 위코드와 동일
c2 = MyClass()
MyClass.set(c2, 'egg')
print MyClass.get(c2)
print c2.value

class Simple:	
	pass

c = MyClass()
s1 = Simple()
#MyClass.set(s1, 'egg')  #자신의 레퍼런스만 가질 수 있다. -> error

#메소드 호출 종류
#	Unbound method call: 클래스 객체를 이용한 메소드 호출
#	ex) Myclass.set(c, 'egg')
#	Bound method call: 인스턴스 객체를 통한 메소드 호출
#	(self 인자는 호출받는 객체가 자동으로 할당)
#	ex) c.set('egg')

#클래스 내부에서의 메소드 호출
class MyClass:
	def set(self, v):
		self.value = v
	def incr(self):
		self.set(self.value + 1)  #내부 메소드 호출
	def get(self):
		return self.value

c = MyClass()
c.set(1)
print c.get()
c.incr()
print c.get()

#만약 위 코드에서 self.set(self.value + 1)를 set(self.value + 1)으로 바꾸면 set()을 정적영역에서 찾는다.
#selt가 없으면 메소드를 class 밖에서 찾음
#메소드 내 다른 메소드, 인스턴스 호출시 반드시 self사용
def set(i):
	print 'set function - ', i

class MyClass:
	def set(self, v):
		self.value = v
	def incr(self):
		set(self.value + 1)  #정적 영역에 존재하는 set()호출
	def get(self):
		return self.value

c = MyClass()
c.set(1)
print c.get()
c.incr()
print c.get()

#static method: 인스턴스 객체와 무관하게 클래스 이름공간에 존재하는 메소드로 클래스 이름을 이용하여 직접 호출할 수 있는 메소드
#	[주의] 해당 클래스의 인스턴스를 통해서도 호출 가능
#	장식자(Decorator) @staticmethod활용
class D:
	@staticmethod
	def spam(x, y):  #self가 없다.
		print 'static method', x, y

D.spam(1, 2)  #인스턴스 객체없이 클래스에서 직접 호출
print
d = D()
d.spam(1, 2)  #인스턴스 객체를 통해서도 호출 가능(비추천)

#class method: 인스턴스 객체와 무관하게 클래스 이름공간에 존재하는 메소드로 클래스 이름을 이용하여 호출하며 첫 인수로 클래스 객체를 자동으로 받는 메소드
#	[주의] 헤당 클래스의 인스턴스를 통해서도 호출 가능
#	장식자(Decorator) @classmethod활용
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
	c_mem = 100  #class member: 클래스 이름공간에 생성, 모든 인스턴스들에 의해 공유
	def f(self):
		self.i_mem = 200  #instance member: 인스턴스 이름공간에 생성, 각각의 인스턴스마다 독립성 보장
	def g(self):
		print self.i_mem
		print self.c_mem

print Var.c_mem  #클래스 객체를 통하여 클래스 멤버 접근

v1 = Var()  #인스턴스 생성
print v1.c_mem  #인스턴스를 통하여 클래스 멤버 접근
v1.f()  #인스턴스 멤버 생성
print v1.i_mem  #인스턴스를 통하여 인스턴스 멤버 접근

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
#__init__: 생성자
#	객체가 생성될 떄 자동으로 호출
#	self인자가 정의되어야함
#__del__: 소멸자
#	객체가 소멸(메모리에서 해제)될떄 자동으로 호출
#	self인자가 정의되어야함
#	개발자가 특별히 작성하지 않아도될 메소드
#	이유: 파이썬에서는 메모리나 기타 자원들의 해제가 자동으로 되기 때문
#	[참고] '__'의 의미: 예약된 이름
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

#인자를 받는 생성자 호출가능
class Integer:
	def __init__(self, i):
		self.i = i
	def __str__(self):  #print나 str() 호출에 대응되는 메소드
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

