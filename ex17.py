# -*- coding: utf-8 -*-

#Naming Space or Scope: 이름이 존재하는 장소
#파이썬은 실행 시간에 각 이름들을 적절한 이름 공간에 넣어 관리
#이름 공간(스코프)의 종류
#	지역(Local): 각 함수 내부
#	전역(Global): 모듈(파일) 내부
#	내장(Built-in): 파이썬 언어 자체에서 정의한 영역
#변수가 정의되는 위치에 의해 스코프가 결정
#	파이썬에서 변수 정의
#		변수가 l-value로 사용될 때
#	함수 내에서 정의되면 해당 함수의 지역변수가 된다.
#변수가 r-value로 사용될 때 해당 변수의 값을 찾는 규칙
#	L -> G -> B

#g, h는 전역 변수
g = 10
h = 5

def f(x):
	h = x + 10  #h, x(local)
	b = h + x + g  #b, x, h(local), g(global)
	return b

print f(h)  #f(5). 함수 호출시 사용되는 변수는 해당 위치의 스코프에서 값을 찾음
print h  #global 
print

#함수 내부에서 전역변수를 직접 사용하고자 할 때 global키워드 활용
h = 5

def f(x):  #a는 local
	global h  #global variable use
	h = x + 10
	return h

print f(10)
print h  #전역 변수 h값이 함수 내에서 변경되었음

#동일 함수내에서 동일한 변수가 지역, 전역변수로 동시에 활용될 수 없음
#	함수 내에서 정의되는 변수는 지역변수로 간주
#	지역변수로 선언되기 이전에 해당 변수를 사용할 수 없음
#scope error
g = 10

def f():
	global g  #error resolve1 -> global keyword
	#g = 20  #error resolve2 -> local variable
	x = g  #g(global)
	g = 20  #g(local)
	return x

print f()

#특정 공간의 이름목록 얻기
#Name: 변수(객체) 이름
#	함수 이름
#	클래스 이름
#	모듈 이름
#dir(): 함수가 호출된 스코프에서 정의되어 있는 모든 Name들을 문자열 리스트로 반환
#dir(object): object이 지니고 있는 모든 Name들을 문자열 리스트로 반환
#파이썬의 모든 것은 object(함수, 객체, 클래스, 인스턴스, 모듈이름 등)
l = []
print dir(l)

#Nested Scopes: 함수안에 정의되어 있는 함수 내부
#	가장 안쪽의 스코프부터 바깥쪽의 스코프쪽으로 변수를 찾는다.
x = 2
def f():
	x = 1
	def g():
		print x  #1
	g()

f()

#모듈: 파이썬 프로그램 파일로서 파이썬 데이터와 함수등을 정의하고 있는 단위
#	서로 연관있는 작업을 하는 코드를 묶어서 독립성을 유지하되 재사용 가능하게 만드는 단위
#	모듈을 사용하는 측에서는 모듈에 정의된 함수나 변수 이름을 사용
#모듈의 종류
#	표준 모듈
#		파이썬 언어 패키지안에 기본적으로 포함된 모듈
#		대표적인 표쥰 모듈 예: math, string
#	사용자 생성 모듈: 개발자가 직접 정의한 모듈
#	써드파티 모듈: 다른 업체나 개인이 만들어서 제공하는 모듈
#모듈이 정의되고 저장되는 곳은 파일
#	파일: 모듈 코드를 저장하는 물리적인 단위
#	모듈: 논리적으로 하나의 단위로 조직된 코드의 모임
#파이썬 모듈의 확장자: .py
#다른곳에서 모듈을 사용하게 되면 해당 모듈의 .py는 바이트 코드로 컴파일 되어 .pyc로 존재
#.pyc가 있으면 .py가 없더라도 .pyc를 활용하여 import가능

#module definition
import mymath

print dir(mymath)  #mymath에 정의된 이름들 확인. __가 없는 식별자는 평범한 식별자
print mymath.mypi  #mymath 안에 정의된 mypi를 이용
print mymath.add(1, 10)  
print mymath.area(10)  #mymath 안에 정의된 area를 사용

import string
print dir(string)

#함수와 모듈
#	함수: 파일 내에서 일부 코드를 묶는 것
#	모듈: 파일단위로 코드를 묶는 것. 비슷하거나 관련된 일을 하는 함수나 상수값들을 모아서 하나의 파일에 저장하고 추후에 재사용하는 단위
#모듈 사용의 이점
#	코드의 재사용
#	개발시 전체 코드를 모듈 단위로 분리하여 설계함으로써 작업의 효율 증가
#	이름공간을 제공함으로써 동일한 이름이 각 모듈마다 독립적으로 정의
#별도 파일내에 파이썬 코드 저장(모듈 코딩할 때)한글 처리
#	1번쨰 줄에 # -*- coding: utf-8 -*-
#모듈은 하나의 독립된 이름 공간을 확보하면서 정의

#name space
#1. module
string.a = 1  #string모듈 밖에서 새로운 변수를 정의하여 삽입. 비추
print string.a

#2. class, object
class C:
	a = 2
	pass

c = C()  #클래스 인스턴스 객체 생성
c.a = 1  #instance inner variable
print c.a  ##instance variable
print c.__class__.a  #class variable
print C.a  #class variable

#3. method
#method 안에서 선언된 변수는 밖에서 조작 불가
x = 10
def f():
	a = 1
	b = 2
f.c = 1
print f.c
#print f.a  #error

#module search path
#1. in memory -> import
import string

#2. current directory

#3. PYTHON PATH

#4. 표준 라이브러리 디렉토리들

#code내에서 모듈 검색 경로 확인
import sys
print sys.path

#code내에서 모듈 검색 경로 추가
sys.path.append('~/Dev')
print sys.path
