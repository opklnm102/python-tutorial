# -*- coding: utf-8 -*-

#list align
l = [1, 5, 3, 9, 8, 4, 2]
l.sort()  #리스트 자체를 변경(반환X)
print l

#파이썬은 디폴트로 cmp(a,b) 내장 함수를 이용하여 정렬방식 결정
#cmp(a,b) -> sort()의 핵심 내장함수
#	if a < b: return -1
#	if a > b: return 1
#	if a == b: return 0
print cmp(1,2)  #a < b -> -1
print cmp(5,2)  #a > b -> 1
print cmp('abc', 'abc')  #a == b -> 0

#기본 정렬 방식 변경. cmp()를 직접만들어 인자로 넣는다.
def mycmp(a1, a2):  #대소관계에 따른 순서를 반대로 바꾸었음
	return cmp(a2, a1)

l = [1, 5, 3, 2, 4, 6]
l.sort(mycmp)  #역순으로 정렬
print l

#여러 튜플을 요소로 지닌 리스트인 경우, 튜플의 첫번째 값이 아닌 다른위치에 있는 값을 기준으로 정렬
def cmp_1(a1, a2):
	return cmp(a1[1], a2[1])

def cmp_2(a1, a2):
	return cmp(a1[2], a2[2])

l = [('lee', 5, 38), ('kim', 3, 28), ('jung', 10, 36)]
l.sort()
print 'sorted by name: ', l

l.sort(cmp_1)
print 'sorted by experience: ', l

l.sort(cmp_2)
print 'sorted by age: ', l

#sort()의 인자로 reverse값을 받을 수 있다.
l = [1, 6, 3, 8, 6, 2, 9]
l.sort(reverse = False)  # == l.sort(). default. 오름차순 정렬
print l

l.sort(reverse = True)  #내림차순 정렬
print l

#sort()의 인자로 key에 함수를 넣어줄 수 있다.
#key에 함수가 할당되어 있으면 비교함수 호출 직전에 key함수를 먼저 호출
l = ['123', '34', '56', '2345']
l.sort()  #문자열에 대해 비교
print l

l.sort(key = int)  #숫자에 대해 비교. 비교하는 순간 정수로 바꾸고 문자열 반환
print l

#sorted(): 자체 내용 변경 없이 정렬되어진 새로운 리스트 반환
l = [1, 6, 3, 8, 6, 2, 9]
newList = sorted(l)
print newList
print l

for element in sorted(l):
	print element,

#sorted() 2번째 인자로 cmp함수 지정 가능
print 
l = [1, 5, 3, 2, 4, 6]
print sorted(l, mycmp)  #역순 정렬
print l

#reverse, key 지정 가능
print sorted(l, reverse = True)  #역순 정렬

l = ['123', '34', '56', '2345']
print sorted(l, key=int)  #정수로 비교

#reversed(): 역순 리스트 반환
l = [1, 6, 3, 8, 6, 2, 9]
print l.reverse()  #자체를 역순으로. 반환X
print l

for element in l:
	print element + 2,

print
l.reverse()
print l

for element in reversed(l):
	print element + 2,
print
print l

#List Comprehension(리스트 내포)
print
print 'List Comprehension'

#general. 일반적인 리스트 생성법
l = []
for i in range(10):
	l.append(i*i)
print l

#list comprehension(리스트 내포): 리스트안에 실제 포함되어야 하는 원소가 식으로 들어감
#식의 결과로 하나의 원소가 나와야 하며 2개 이상일 경우 튜플등으로 감싸야 한다.
#ex) [x, y for x in seq1 for y in seq2] -> X
#	 [(x, y) for x in seq1 for y in seq2] -> O
l = [k * k for k in range(10)]  #for의 변수가 식의 변수와 동일해야 함
print l

#홀수의 제곱만 리스트로 형성
#general
l = []
for k in range(10):
	if k % 2:
		l.append(k * k)
print l

#list comprehension
l = [k * k for k in range(10) if k % 2]
print l

#20보다 작은 2의 배수와 3의 배수에 대해 그 두수의 합이 7의 배수인 것들에 대해
#그 두수의 곱을 출력하는 코드
l = [(i, j, i*j) for i in range(2, 20, 2) for j in range(3, 20, 3) if (i + j) % 7 == 0]
print l

#두개의 시퀀스 자료형에 대해 각각의 원소에 대한 쌍을 튜플 형태로 만들면서
#리스트에 저장하는 코드
seq1 = 'abc'
seq2 = (1, 2, 3)
print [(x, y) for x in seq1 for y in seq2]

words = 'The quick brown fox jumps over the lazy dog'.split()
print words
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
print stuff
for i in stuff:
	print i

#seq1='abc', seq2=(1,2,3), seq3=[4,5,6]를 입력한 후 각각의 원소에 대한 쌍을 튜플
#형태로 만들면서 리스트에 저장하는 코드를 리스트 내포 형식으로 작성하고 출력
seq1 = 'abc'
seq2 = (1, 2, 3)
seq3 = [4, 5, 6]
l = [(x, y, z) for x in seq1 for y in seq2 for z in seq3]
print l

