# -*- coding: utf-8 -*-

#file I/O

#open(filename, mode)

import os

print os.getcwd()  #cwd(=current working directory)

s = """Its power: Python developers typically report
they are.
zzzzz
fdfd
fdfd"""
f = open('t.txt', 'w')
print type(f)
f.write(s)  #문자열을 파일에 기록
f.close()

f = open('t.txt')
s = f.read()
print s
print

#line단위로 file read
#1. iterator
f = open('t.txt')
i = 1
for line in f:
	print i, ":", line,
	i += 1
f.close()
print

#2. readline()
f = open('t.txt')
line = f.readline()
i = 1
while line:
	print i, ":", line,
	line = f.readline()
	i += 1
f.close()

#3. readlines()
f = open('t.txt')
print f.readlines()
print

f.seek(0)
i = 1
for line in f.readlines():
	print i, ":", line,
	i += 1
f.close()
print

#4. xreadlines()
f = open('t.txt')
print f.xreadlines()
print

f.seek(0)
i = 1
for line in f.xreadlines():
	print i, ":", line,
	i += 1
f.close()
print

#line단위로 file write
#1. writelines()
lines = ['first line\n', 'second line\n', 'third line\n']  #\n필히 넣어줌
f = open('t1.txt', 'w')
f.writelines(lines)
f.close

f = open('t1.txt')
print f.read()
f.close()

#2. write()
lines = ['first line', 'second line', 'third line']
f = open('t.txt', 'w')
f.write('\n'.join(lines))
f.close()

f = open('t1.txt')
print f.read()
f.close()

#
f = open('t.txt')
s = f.read()
n = len(s.split())
print n
f.close()

#기존 파일에 파일 내용 추가
f = open('removeme.txt', 'w')
f.write('first line\n')
f.write('second line\n')
f.close()

f = open('removeme.txt', 'a')
f.write('third line\n')
f.close()

f = open('removeme.txt')
print f.read()

#file pointer random access
name = 't.txt'
f = open(name, 'w+')  # w+(=rw)
s = 'abcdefghijk'
f.write(s)

f.seek(5)  # 5byte move
print f.tell()  #current pointer
print f.read(1)  #1 character read
print f.tell()
print

#redirection
import sys

#1
f = open('t.txt', 'w')
stdout = sys.stdout  #stdout store
sys.stdout = f  #redirection
print 'Sample output'
print 'Good'
print 'Good'
f.close()
sys.stdout = stdout  #stdout restore

f = open('t.txt')
print f.read()
print

#2 >>
print >> sys.stderr, "Warning, action field not supplied"

f = open('t.txt', 'w')
print >> f, 'spam string'
f.close()

f = open('t.txt')
print f.read()
f.close()

#StringIO
import StringIO

f = StringIO.StringIO()
f.write("abc")
f.seek(0)
s = f.read()
print s
print

s2 = f.getvalue()
print s2
print

stdout = sys.stdout
sys.stdout = f = StringIO.StringIO()

print type(f)
print 'Sample output'
print 'Good'
print 'Good'

sys.stdout = stdout

s = f.getvalue()
print s

#Persistence
print 'Persistence'
import pickle

phone = {'tom': 4358382, 'jack': 9465215, 'jim':4343}
List = ['string', 1234, 0.2345]
Tuple = (phone, List)

f = open('pickle.txt', 'w')

pickle.dump(Tuple, f)  #file write
f.close()

f = open('pickle.txt')
x, y = pickle.load(f)  #file read
print x  #dictionary
print y  #list

class Simple:  #가장 단순한 클래스 정의
	pass

s = Simple()  #constructor call
s.count = 10  #instance name space에 변수 생성

f = open('pickle2.txt', 'w')
pickle.dump(s, f)  #instance store
f.close()

f = open('pickle2.txt')
t = pickle.load(f)  #instance restore
print t.__class__
print t.count

#text.txt파일에 대해 각 라인을 읽고 존재하는 단어의 개수를 출력
f = open('pickle.txt', 'r')
i = 1
for line in f.readlines():
	words = line.split()
	print i, ':', len(words)
f.close()
