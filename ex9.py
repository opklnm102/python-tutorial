# -*- coding: utf-8 -*-

#list
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
a[2] = a[2] + 23
print a

a[0:2] = [1, 12]
print a

a[0:2] = [1]
print a

a[0:1] = [1, 2, 3]
print a

a = [1, 12, 123, 1234]
a[0:2] = []
print a

a = [123, 1234]
a[1:1] = ['spam', 'ham']
print a

b = [123, 1234]
b[1:2] = ['spam', 'ham']
print b

a[0:0] = a
print a

a = [1, 2, 3, 4]
del a[0]
print a

del a[1:]
print a

a = range(4)
print a
print a[::2]

del a[::2]
print a

a = range(5)
del a

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

print range(10)  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print range(5, 15)  #[5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print range(5, 15, 2)  #[5, 7, 9, 11, 13]

for el in range(10):
	print el, 'inch = ', el * 2.54, 'centi'

sun, mon, tue, wed, thu, fri, sat = range(7)
print sun, mon, tue, wed, thu, fri, sat

lt = [('one', 1), ('two', 2), ('three', 3)]
for t in lt:
	print 'name = ', t[0], ', num = ', t[1]

for t in lt:
	print 'name = %s, num = %s' % t

for name, num in lt:  #for header
	print name, num

lt = [['one', 1], ['two', 2], ['three', 3]]
for name, num in lt:  #for header
	print name, num

#list method
print
s = [1, 2, 3]

s.append(5)
print s
s.append("abc")
s.append((1, 2))
s.append({'a':100})
print s

s.insert(3, 4)
print s

s.insert(0, "abcd")
print s

s = [1, 2, 3, 4, 5]

print s.index(3)
s.append("abc")
print s
print s.index("abc")

print s.count(2)

s = [1, 2, 2, 2, 2, 2, 2, 3, 4, 5]
print s.count(2)

s = [1, 2, -10, -7, 100]
s.reverse()
print s

s.sort()
print s

s = [10, 20, 30, 40, 50]
s.remove(10)
print s

s = [10, 20, 30, 20, 40, 50]
s.remove(20)
print s

s.extend([60, 70])
print s

s.append([60, 70])
print s

print s.pop()
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
print q.pop(0)

print q

#초기에 내용이 비어있는 리스트를 스택으로 활용하여 정수 1부터 차례대로 10까지
#스택에 쌓고 마지막에 삽입된 정수부터 4개의 수를 꺼내오는 프로그램을 작성
stack = []
for element in range(1,11):
	stack.append(element)
	print stack

for idx in range(4):
	print stack.pop()


	