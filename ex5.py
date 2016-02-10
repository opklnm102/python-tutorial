# -*- coding: utf-8 -*-

#산술
print 1 + -1  #0
print 2 ** 3  #8, 지수연산
print 2 ** 2 ** 3  #256
print 2 ** (2 ** 3)  #256
print (2 ** 2) ** 3  #64

print
print 5 / 2  #2
print 5 % 2  #1
print -5 / 2  #-3
print -5 % 2  #1
print 5 % 2 + 1  #2
print 5 % (2 + 1)  #2

print
print 3 + 5  #8
print 3 + 5.0  #8.0  정수 + 실수의 결과는 실수

print 5 / 2.0  #정수 / 실수의 결과는 실수
print 5 / 2

a = 5 / 3  #정수
b = 5 % 3

print a, b
print divmod(5,3)  #(1,2) 몫과 나머지를 튜플로

print
print 5 / 3  #소수점 이하를 버림
print 5 // 3  #몫을 구해서 출력
print 10.52 / 3
print 10.52 // 3

print 7 / 4
print -7 / 4  #-2
print -(7/4)  #-1

print 2 + 3 * 4  #14
print (2 + 3) * 4  #20

print 4 / 2 * 2  #4


#관계: 객체가 지닌 값의 크기(대소)를 비교하여 True, False를 반환
print
print 6 == 9  #두 객체가 동일한지를 판단
print 6 != 9  #두 객체 값이 달라야 True
print 1 > 3
print 4 <= 5

a = 5
b = 10
print a < b

a = 5
b = 10
print 0 < a < b  #0 < a and a < b

#같은 자료형일 때'사전순서'
print 'abcd' > 'abc'
print (1,2,4) < (2,1,0)
print [1,3,2] == [1,2,3]
print (1, 2, 4) == (1, 2, 4)  #내용이 동일하므로 True

#다른 자료형일 때 '자료형간의 크기 관계'
# 숫자 < 사전 < 리스트 < 문자열 < 튜플
print
print 999999999999999L < 'abc'  #True
print {3:2} < [1, 2, 3] < (1,2,3)  #True

L = [1,2,3,'abc','a','z',(1,2,3),[1,2,3],{1:2},['abc']]
L.sort()  #리스트의 원소를 크기로 정렬
print L

print
x = [1,2,3]
y = [1,2,3]
z = y

print x == y
print x == z
print x is y
print x is z
print y is z

#논리
print
a = 20
b = 60
print a > 10 and b < 50
print a > 10 or b < 50

print True + 1
print False + 1
print False * 75
print True * 75

#bool()
print bool(0)  #False 정수 0은 거짓
print bool(1)  #Ture
print bool(100)  #Ture
print bool(-100)  #Ture
print
print bool(0.0)  #False 실수 0.0은 거짓
print bool(0.1)  #Ture

print bool('abc')  #True
print bool('')  #False
print
print bool([])  #False
print bool([1,2,3])  #True
print
print bool(())  #False
print bool((1,2,3))  #True
print
print bool({})  #False
print bool({1:2})  #True
print
print bool(None)  #False

print 1 and 1  #1 True
print 1 and 0  #0 False
print 0 or 0  #0 False
print 1 or 0  #1 True
print
print [] or 1  #1 True
print [] or ()  #() False
print [] and 1  #[] False

print 1 and 2  #2 True
print 1 or 2  #1 True
print
print [[]] or 1  #[[]] True
print [{}] or 1  #[{}] True
print '' or 1  #1 True

print not(True)
print not(1 and 2)
print not('' or 1)

#연산자 우선순위에 의존하기보다 적절한 괄호 활용이 필요
print 2 * 2 + 1 / 5
print (2 * 2) + (1 / 5)

