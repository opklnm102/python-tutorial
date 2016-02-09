import sys

# int
a = 23
b = 023
c = 0x23

print type(a), type(b), type(c)
print a, b, c

print sys.maxint  #max int range check

# float
a = 1.2
b = 3.5e3  #3.5 * 10^3 = 3500.0
c = -0.2e-4  #-0.2 * (1/10000) = -2 * (1/100000) = -2e-5

print type(a), type(b), type(c)
print a, b, c

# long: int의 최대 범위를 벗어난 수
#메모리가 허용하는한 유효자리 수가 무한
#L을 붙이거나, maxint를 초과하면 자동으로
h1 = 122L
h2 = 2313232333333333333333333333333333

print type(h1), type(h2)
print h1, h2

# complex: 실수부와 허수부가 각각 계산
a = 10 + 20j
print a
print type(a)

b = 10 + 5j
print b
print a + b

#수치 자료형의 치환
x = 1  #x는 1(객체)을 가리키는 레퍼런스
x = 2  #x가 2(객체)를 가리키고 1은 garbage가 되어 수집됨

#수치 연산과 관련된 내장함수
print
print abs(-3)  #절대값
print int(3.141592)  #정수형 출력
print int(-3.1415)
print int(-3.9999)
print long(3)  #롱형 출력(L안나타남)
print float(5)  #실수형 출력
print complex(3.4, 5)  #복소수형 출력
print complex(6)  #6+0j와 같이 실수부만 나타남
print divmod(5, 2)  #(a를 b로 나눈 몫, 나머지)
print pow(2, 3)  #a의 b승값
print pow(2.3, 3.5)  #실수도 입력가능


# math module의 수치연산 함수
import math

print
print math.pi  #파이
print math.e  #지수
print math.sin(1.0)  #1.0라디안에 대한 싸인
print math.sqrt(2)  #제곱근

#원의 넓이
r = 5.0
a = math.pi * r * r
print a

#각도가 60도일 때 라디안값 출력
degree = 60.0
rad = math.pi * degree / 180.0
print math.sin(rad), math.cos(rad), math.tan(rad)


# string
print 'Hello "World"'  #Hello "World"
print "Hello 'World'"  #Hello 'World'

#여러줄 출력
multiline = '''
To be, or not to be
that is the question
'''
print multiline

multiline2 = """
To be, or not to be
that is the question
"""
print multiline2

#인덱싱: [index], [-index](역순)
s = "Hello World!"
print s[0]  #H
print s[1]  #e
print s[-1]  #!
print s[-2]  #d

#슬라이싱(자르기): [start(포함):end(제외): step]
print s[1:3]  #el
print s[0:5]  #Hello
print s[1:6:3]  #eo

print s[1:]  #ello World!, 1부터 끝까지
print s[:3]  #Hel, 처음부터 3까지
print s[:]  #Hello World!, 처음부터 끝까지
print s[::2]  #HloWrd, 처음부터 끝까지 2개의 step
print s[::-1]  #!dlroW olleH, 문자열 거꾸로

#문자열은 내부 내용 변경 불가능
#ex) s[0] = 'q'
s = 'h' + s[1:]  #슬라이싱을 활용해 문자열 새로 구성
print s

print 'Hello' + ' ' + 'World'  #문자열 연결
print 'Hello ' * 10  #숫자만큼 문자열 반복
print '-' * 60 

print len(s)  #문자열의 길이

#문자열내 포함 관계 여부
#A in B: B안에 A가 있다.
#A not in B: B안에 A가 없다.
print 'World' in s
print 'World' not in s
print ' ' in s  #문자열안에 공백이 있다.


