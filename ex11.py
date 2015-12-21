# -*- coding: utf-8 -*-

t1 = ()
t2 = (1, 2, 3)

t3 = 1, 2, 3  # == (1, 2, 3)
print type(t1), type(t2), type(t3)

r1 = (1)  #no tuple
print r1
print type(r1)
print

r1 = (1, )  #tuple
r2 = 1,  #tuple
print r1
print r2
print type(r1)
print type(r2)

t = (1, 2, 3)
print t * 2
print t + ('PyKUG', 'users')
print t
print 

print t[0], t[1:3]
print len(t)
print 1 in t

# t[0] = 100  #error -> 변경 불가능

t = (12345, 54321, 'Hello!')  #tuple을 원소로
u = t, (1, 2, 3, 4, 5)  # == (t, (1, 2, 3, 4, 5))
print u

t2 = [1, 2, 3]  #list를 원소로
u2 = t2, (1, 2, 4)
print u2

t3 = {1:"abc", 2:"def"}  #dictionary를 원소로
u3 = t3, (1, 2, 3)
print u3

x, y, z = 1, 2, 3  # == (1, 2, 3)
print type(x), type(y), type(z)
print x, y, z

x = 1
y = 2
x, y = y, x  #tuple을 이용한 swap
print x, y

#Packing <-> unPacking
#Packing: 하나의 튜플안에 여러개의 데이터를 넣는 작업(=여러개의 객체를 하나의 변수에 묶는 것)
print 'Packing'
t = 1, 2, 'hello'  #(1, 2, 'hello')

#unPacking: 하나의 튜플에서 여러개의 데이터를 한꺼번에 꺼내 각각변수에 할당하는 작업(=묶여 있는 객체를 푸는 것)
x ,y ,z = t
print x, y, z

l = ['foo', 'bar', 4, 5]
print l
[x, y, z, w] = l
print x, y, z, w

T = (1, 2, 3, 4, 5)
L = list(T)
L[0] = 100
print L

T = tuple(L)
print T


#tuple 사용 용도

#1 multiple return value
def calc(a, b):
	return a + b, a * b

x, y = calc(5, 4)
print x, y

#2 string formating
print 'id : %s, name : %s' % ('gslee', 'GongSeong')

#3 고정된 값을 쌍으로 표현하는 경우
d = {'one':1, 'two':2}
print d.items()

#집합 자료형
a = set([1, 2, 3])
print type(a)
print a
print 

a = set([1, 2, 2, 3])  #duplication removal
print type(a)
print a
print 

b = set((1, 2, 3))
print type(b)
print b
print

c = set({'a':1, 'b':2, 'c':3})
print type(c)
print c
print

d = set({'a':1, 'b':2, 'c':3}.values())
print type(d)
print d

print set()
print set([1, 2, 3, 4, 5])
print set([1, 2, 3, 2, 3, 4])
print set('abc')
print set([(1, 2, 3), (4, 5, 6)])
# print set([[1, 2, 3], [4, 5, 6]])  #error -> 변경가능한 list는 집합의 원소가 될 수 없다.

A = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
print len(A)
print 5 in A
print 10 not in A

B = set([4, 5, 6, 10, 20, 30])
C = set([10, 20, 30])

print C.issubset(B)  #
print c <= B
print B.issuperset(C)  #
print B >= C

A = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
B = set([4, 5, 6, 10, 20, 30])

print A.union(B)  #  == A | B
print A
print A.intersection(B)  #  == A & B
print A
print A.difference(B)  # == A - B
print A
print A.symmetric_difference(B)  #  == A ^ B
print A

#copy
D = A.copy()
print D
print

print A == D  #
print A is D  #

# print A[0]  #error -> no sequence
# print A[1:4]  #error -> no sequence
# print A.sort()  #error -> no sequence
print list(A)
print tuple(A)

for element in A:
	print element,
print

#update
A = set([1, 2, 3, 4])
B = set([3, 4, 5, 6])

A.update(B)  # (|=)       
print A

A.intersection_update([4, 5, 6, 7, 8])  # (&=)
print A

A.difference_update([6, 7, 8])  # (-=)
print A

A.symmetric_difference_update([5, 6, 7])  # (^=)
print A

A.add(8)  #element add
print A

A.remove(8)  #element remove, 없는 원소를 제거하면 KeyError
print A

A.discard(10)  #remove와 같으나 error가 발생하지 않음

A.pop()  #임의의 원소 하나 꺼내기(random)
print A

A.clear()  #원소 모두 없애기
print A

#t1=[1,2,3,4,5]과 t2=[3,4,5,6,7]를 입력한 후 두개의 리스트에 존재하는 원소들
#모두 지니는 새로운 리스트 t3를 구성함에 있어서 t1과 t2에 중복되어 속한 원소를
#배제한 리스트를 구하여 출력
t1 = [1, 2, 3, 4, 5]
t2 = [3, 4, 5, 6, 7]
s1 = set(t1)
s2 = set(t2)
s3 = s1.symmetric_difference(s2)
t3 = list(s3)
print t3

