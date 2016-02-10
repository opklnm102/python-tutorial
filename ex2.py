# -*- coding: utf-8 -*-

#예약어 종류 알아보기
import keyword
print keyword.kwlist
print len(keyword.kwlist)  #len(): 길이를 반환하는 내장함수(built-in function)

#built-in function: 별도의 Module추가 없이 기본적으로 제공되는 함수들
#abs(n): 수치형 자료를 절대값으로 반환하는 내장함수
print abs(-3)  #3

#max(s): 시퀀스 자료형(문자열, 리스트, 튜플)을 입력받아 그 자료가 지닌 원소 중 최대값을 반환
print max([1,2,3])  #3

#min(s): 시퀀스 자료형(문자열, 리스트, 튜플)을 입력받아 그 자료가 지닌 원소 중 최소값을 반환
print min("Python")  #문자열 중 아스키코드값이 가장 작은 문자 반환

#pow(x,y): 수치형 자료형 x,y에 대해 x의 y승을 반환
print pow(2,4)  #16

#chr(i): 정수 형태의 ASCII코드 값을 입력받아 해당하는 문자 반환
#i의 범위: 0~255까지
print chr(65)  #A

#str(object): 임의의 객체 object에 대해 해당 객체를 표현하는 문자열 반환
print str(3)  #3

#range([start,] stop [,step]): 수치형 자료형으로 인자를 입력받아 해당 범위의 정수를 리스트로 반환
#인수가 하나인 경우(stop) 0~stop-1까지의 정수 리스트 반환
print range(10)  #[0,1,...,9]

#인수가 2개인경우(start,stop) start~stop-1까지의 정수 리스트 반환
print range(3, 10)  #[3,4,...,9]

#인수가 3개인 경우(start,stop,step) start~stop-1까지의 정수를 사이 거리가 step인 것들만 반환
print range(3, 10, 2)  #[3,5,7,9]

#type(a): a(객체)의 자료형을 반환
print type(range(3, 10, 2))  #<type 'list'>

print type (-3)  #<type 'int'>

print type('3')  #<type 'str'>

#예약어, 내장함수, 모듈이름을 변수명으로 사용하지 말것
str = 'abd'  #본래의 기능을 상실한다.
print str
del str  #변수삭제

print str([3,43])
print str

#변수에 값이 할당될 때 변수가 생성, 생성시 타입이 정해짐
a = 1
b = 3
c = 4

#연속라인: '\'-> 나눠진 줄을 한줄로 인식하도록함.
#코딩이 길어져 한 화면에 나타나지 않을 때 사용
if(a == 1) and \
(b == 3):
	print 'connected lines'

#변수 생성
e,f = 3,4
print e,f

a = [1, 2, 3]
b = [10, a, 20]
print a
print b

a[1] = 1000
print a
print b

b[1] = 3
print a
print b

#두문장을 이어 쓸 때 ';'사용, 가독성 때문에 자주 활용X
print 1; print 2

print 1 + 3, print 2 + 2

#할당문
#두변수의 값을 swap하는 방법
e = 3.5; f = 5.6
e,f = f,e
print e, f

#확장 할당문
#+=, -=, *=, /= 
a = 1
a += 4
print a

a *= 2 + 3  #(2+3 수행 후 a에 곱한다.)

#객체의 변수는 해당 객체의 레퍼런스를 지닌다.
#파이썬에서는 모든것이 객체
#변수는 객체를 가리키는 레퍼런스
a = 1  #a는 변수이름, 1은 객체
a = [1, 2, 3]  #1, 2, 3을 가리키는 레퍼런스가 존재하는 리스트를 a가 가리킴

#콘솔입력
#raw_input(): 문자열 입력 내장함수
name = raw_input('name?')

#int(): 문자열을 정수로 변환하는 내장함수
n = int(raw_input('int>> '))

#input(): 정수, 실수, Expression입력 내장함수
i = input('int>> ')

#콘솔출력
#print: 화면에 자료를 출력하는 보편적인 statement, 기본적으로 줄바꿈
#여러 자료를 한꺼번에 출력할 때는 ','(한칸 띄어줌)사용
print 1,
print 2

#+연산자는 숫자와 문자열에 대한 연산지원X
print str(12) + 'spam'

