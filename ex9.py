# -*- coding: utf-8 -*-

#list: 시퀀스 자료형이면서 변경가능(Mutable)
#인덱싱, 슬라이싱, 연결, 반복, 멤버쉽테스트 지원
l = []
l = [1, 2, "Great"]
print l[0], l[-1]
print l[1:3], l[:]
print

L = range(10)
print L[::2]
print

print l * 2
print l + [3, 4, 5]
print len(l)
print 4 in l
print

a = ['spam', 'eggs', 100, 1234]
a[2] = a[2] + 23  #a[2]의 자리에 새로운 값을 할당
print a

#리스트 원소에 대한 슬라이스 치환
a[0:2] = [1, 12]  #동일한 크기에 대한 슬라이스 치환
print a  #[1, 12, 123, 1234]

a[0:2] = [1]  #서로 다른 크기에 대한 슬라이스 치환
print a  #[1, 123, 1234]

a[0:1] = [1, 2, 3]  #서로 다른 크기에 대한 슬라이스 치환
print a  #[1, 2, 3, 123, 1234]

#리스트 원소에 대한 슬라이스 삭제
a = [1, 12, 123, 1234]
a[0:2] = []
print a  #[123, 1234]

a = [123, 1234]
a[1:1] = ['spam', 'ham']  #첫번째 인덱스에 삽입
print a

b = [123, 1234]
b[1:2] = ['spam', 'ham']  #1번쨰 원소에 대한 치환
print b

a[0:0] = a  #리스트 맨앞에 자기자신을 삽입
print a

#del: 리스트 요소 삭제
a = [1, 2, 3, 4]
del a[0]  #0번 인덱스 요소 삭제
print a  #[2, 3, 4]

del a[1:]  #1번 인덱스부터 끝까지 삭제
print a  #[2]

a = range(4)
print a  #[0, 1, 2, 3]
print a[::2]  #[0, 2]

del a[::2]
print a  #[1, 3]

#리스트 자체에 대한 삭제. 리스트를 가리키는 레퍼런스를 지닌 변수 a삭제
a = range(5)
del a

#중첩 리스트: 리스트 안에 요소로 리스트를 지닌 리스트
s = [1,2,3]
t = ['begin', s, 'end']
print t

print t[1][1]
print t[1]

s[1] = 100
print t

L = [1, ['a', ['x', 'y'], 'b'], 3]
print L[0]  #1
print L[1]  #['a', ['x', 'y'], 'b']
print L[1][1]  #['x', 'y']
print L[1][1][1]  #y

#range(start[, stop][, step]). 순차적인 정수 리스트 만들기
print range(10)  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print range(5, 15)  #[5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print range(5, 15, 2)  #[5, 7, 9, 11, 13]

for el in range(10):
	print el, 'inch = ', el * 2.54, 'centi'

sun, mon, tue, wed, thu, fri, sat = range(7)
print sun, mon, tue, wed, thu, fri, sat

#리스트 안의 원소가 튜플일 때 for문을 사용하여 값 추출
lt = [('one', 1), ('two', 2), ('three', 3)]
for t in lt:
	print 'name = ', t[0], ', num = ', t[1]

#밑의 코드가 더 효츌적. 문자열 포맷팅 이용
for t in lt:
	print 'name = %s, num = %s' % t

#for문의 헤더에서 튜플 원소 추출
for name, num in lt:  #for header
	print name, num

#리스트안의 원소가 리스트여도 동일하게 사용
lt = [['one', 1], ['two', 2], ['three', 3]]
for name, num in lt:  #for header
	print name, num

#list method
print
s = [1, 2, 3]

s.append(5)  #s리스트 뒤에 정수 5추가
print s
s.append("abc")
s.append((1, 2))
s.append({'a':100})
print s

s.insert(3, 4)  #3인덱스 위치에 정수 4추가
print s

s.insert(0, "abcd")
print s

s = [1, 2, 3, 4, 5]

print s.index(3)  #값 3의 인덱스 반환
s.append("abc")
print s
print s.index("abc")

print s.count(2)  #값 2의 개수 반환

s = [1, 2, 2, 2, 2, 2, 2, 3, 4, 5]
print s.count(2)

s = [1, 2, -10, -7, 100]
s.reverse()  #순서 뒤집기(반환X)
print s

#python의 소팅 알고리즘: Timsort (변형된 merge sort)
#- 참고: http://orchistro.tistory.com/175
s.sort()  #정렬(반환X)
print s

s = [10, 20, 30, 40, 50]
s.remove(10)  #원소 10 삭제
print s

s = [10, 20, 30, 20, 40, 50]
s.remove(20)  #원소가 여러개면 첫번째 것만 삭제
print s

s.extend([60, 70])  #기존 리스트 s뒤에 병합. 리스트 자체로
print s

s.append([60, 70])  #리스트가 원소로 들어감. 중첩 리스트 됨
print s

print s.pop()  #마지막 원소를 뺌
print s

#list stack
print 'list stack'
s = [10, 20, 30, 40, 50]
s.append(60)
print s

print s.pop()
print s

#list queue
print 'list queue'
q = [10, 20, 30, 40, 50]
q.append(60)
print q.pop(0)  #0번 인덱스의 원소를 뺌

print q

#초기에 내용이 비어있는 리스트를 스택으로 활용하여 정수 1부터 차례대로 10까지
#스택에 쌓고 마지막에 삽입된 정수부터 4개의 수를 꺼내오는 프로그램을 작성
stack = []
for element in range(1,11):
	stack.append(element)
	print stack

for idx in range(4):
	print stack.pop()


	