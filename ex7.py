# -*- coding: utf-8 -*-

#indexing
print '----------indexing-------------'
s = 'abcdef'
l = [100, 200, 300]
print s[0]
print s[1]
print s[-1]
print
print l[1]
l[1] = 900
print l[1]

#slicing
print
print '----------slicing-------------'
s = 'abcdef'
L = [100, 200, 300]
print s[1:3]
print s[1:]
print s[:]
print s[-100:100]
print
print L[:-1]
print L[:2]

#extended slicing
print
print '----------extended slicing-------------'
s = 'abcd'
print s[::2]
print s[::-1]

#concatenation  +
print
print '----------concatenation-------------'
s = 'abc' + 'def'
print s

L = [1,2,3] + [4,5,6]
print L


#repition  *
print
print '----------repition-------------'
s = 'abc'
print s * 4

L = [1,2,3]
print L * 2

#membership test  in
print
print '----------membership test-------------'
s = 'abcde'
print 'c' in s

t = (1,2,3,4,5)
print 2 in t
print 10 in t
print 10 not in t

print 'ab' in 'abcd'
print 'ad' in 'abcd'
print ' ' in 'abcd'
print ' ' in 'abcd '

#length
print
print '----------length-------------'
s = 'abcde'
l = [1,2,3]
t = (1,2,3,4)
print len(s)
print len(l)
print len(t)

#for~in
print
print '----------for~in-------------'
for c in 'abcd':
	print c,


#string
print
s = ''
str1 = 'Python is great!'
str2 = "Yes, it is."
str3 = "It's not like any other languages"
str4 = 'Don\'t walk. "Run"'
print str1
print str2
print str3
print str4

long_str = "This is a rather long string \
ontaining back slash and new line\nGood!"
print long_str


multiline = """dddddddddddddddddddddddddddddddddddddddddddddddd
ddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddd
dddddddddddddddddddddddddddddddddddddddddddddddddd"""
print multiline

print
ml = '''ffffffffffffffffffffffffffffffffffffffff
fffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffff'fffffffffffff
fffffffffffffffffffffffffffffffffffffffff'''
print ml

print
print '\\abc\\'
print 'abc\tdef\taghi'
print 'a\nb\nc'

print
str1 = 'First String'
str2 = 'Second String'
str3 = str1 + ' ' + str2
print str3
print str1 * 3
print str1[2]
print str1[1:-1]
print len(str1)
print str1[0:len(str1)]  # == str1[:]

#string modify
print 
s = 'spam and egg'
s = s[:4] + ', chese, ' + s[5:]
print s

#uni code
print
print u'Spam and Egg'
a = 'a'
b = u'bc'
print type(a)
print a
print type(b)
print b
c = a + b
print type(c)
print c

print u'Spam \uB610 Egg'

a = unicode('한글','utf-8')
print type(a)
print a

print len('한글과 세종대왕')
print len(unicode('한글과 세종대왕','utf-8'))
print len(u'한글과 세종대왕')

u = unicode('한글과 세종대왕','utf-8')

print u[0]
print u[1]
print u[:3]
print u[4:]
print u[::-1]
print
u2 = u'한글과 세종대왕'
print u2[0]
print u2[1]
print u2[:3]
print u2[4:]
print u2[::-1]
print
u3 = '한글과 세종대왕'
print u3[0]
print u3[1]
print u3[:3]
print u3[4:]
print u3[::-1]

#s='A, B, D, E'로서 파이썬 코딩된 문자열 s에 슬라이싱과 연결 연산을 활용하여 
#'A, B, C, D, E'문자열을 s가 지니도록 하고, 이후 문자열 s의 길이를 출력하는 
#프로그램을 작성하세요.

s = 'A,B,D,E'
s = s[:4] + 'C,' + s[4:]
print s
print len(s)
