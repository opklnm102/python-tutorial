# -*- coding: utf-8 -*-

#list align
l = [1, 5, 3, 9, 8, 4, 2]
l.sort()
print l

print cmp(1,2)  #a < b -> -1
print cmp(5,2)  #a > b -> 1
print cmp('abc', 'abc')  #a == b -> 0

def mycmp(a1, a2):
	return cmp(a2, a1)

l = [1, 5, 3, 2, 4, 6]
l.sort(mycmp)
print l

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

l = [1, 6, 3, 8, 6, 2, 9]
l.sort(reverse = False)  # == l.sort()
print l

l.sort(reverse = True)
print l

l = ['123', '34', '56', '2345']
l.sort()
print l

l.sort(key = int)
print l

l = [1, 6, 3, 8, 6, 2, 9]
newList = sorted(l)
print newList
print l

for element in sorted(l):
	print element,

print 
l = [1, 5, 3, 2, 4, 6]
print sorted(l, mycmp)
print l

print sorted(l, reverse = True)

l = ['123', '34', '56', '2345']
print sorted(l, key=int)

l = [1, 6, 3, 8, 6, 2, 9]
print l.reverse()
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

#List Comprehension
print
print 'List Comprehension'

#general
l = []
for i in range(10):
	l.append(i*i)
print l

#list comprehension
l = [k * k for k in range(10)]
print l

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

