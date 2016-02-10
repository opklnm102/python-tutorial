# -*- coding: utf-8 -*-

#시퀀스 자료형: 저장된 각 요소를 정수 index를 이용하여 참조 가능한 자료형
#문자열, 리스트, 튜플
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
print s[1:3]  #bc
print s[1:]  #bcdef
print s[:]  #abcdef
print s[-100:100]  #abcedf
print
print L[:-1]  #L[:2]와 동일
print L[:2]  #[100, 200]

#extended slicing. :이 2개 쓰임. step에 해당하는 숫자만큼 인덱스에 차이를 두어 반환
print
print '----------extended slicing-------------'
s = 'abcd'
print s[::2]  #ac
print s[::-1]  #dcba

#concatenation. +. 연결하기
print
print '----------concatenation-------------'
s = 'abc' + 'def'  #2개의 시퀀스를 연결하여 하나로
print s

L = [1,2,3] + [4,5,6]  #하나의 리스트로 반환
print L


#repition. *. 반복하기
print
print '----------repition-------------'
s = 'abc'
print s * 4  #abcabcabcabc

L = [1,2,3]
print L * 2

#membership test. in. 안에 존재하는지 확인
print
print '----------membership test-------------'
s = 'abcde'
print 'c' in s

t = (1,2,3,4,5)
print 2 in t
print 10 in t
print 10 not in t  #10이 t안에 존재하지 않는지 확인

print 'ab' in 'abcd'
print 'ad' in 'abcd'
print ' ' in 'abcd'
print ' ' in 'abcd '

#length. 길이정보
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


#string. '(문장)', "(문장)" 둘다 사용가능
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

#\. 다음라인이 현재 라인의 뒤에 이어짐을 나타냄
long_str = "This is a rather long string \
ontaining back slash and new line\nGood!"
print long_str

#"""(문장)""",'''(문장)''': 여러 줄 문자열
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

#Escape Characters
print
print '\\abc\\'
print 'abc\tdef\taghi'
print 'a\nb\nc'

#문자열 연산
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

#string modify: 여러 Slicing연결 활용. 새로 생성하여 재할당
print 
s = 'spam and egg'
s = s[:4] + ', chese, ' + s[5:]
print s

#uni code: 다국어 문자의 올바른 표현을 위해 지원
print
print u'Spam and Egg'
a = 'a'
b = u'bc'
print type(a)
print a
print type(b)
print b
c = a + b  #일반 + 유니코드 = 유니코드
print type(c)
print c

print u'Spam \uB610 Egg'

a = unicode('한글','utf-8')  #인코딩 방식 지정하여 변환
print type(a)
print a

print len('한글과 세종대왕')
print len(unicode('한글과 세종대왕','utf-8'))  #한글 문자열의 길이를 올바르게 반환
print len(u'한글과 세종대왕')

#유니코드 타입의 한글문자열에 대해서는 인덱싱, 슬라이싱이 올바르게 수행
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

