# -*- coding: utf-8 -*-

s = 'i like programming.'
print s.upper()  #대문자 변환
print s.upper().lower()  #대문자 -> 소문자 변환
print 'I Like Programming'.swapcase()  #대문자 <-> 소문자 변환
print s.capitalize()  #첫문자만 대문자로 변환
print s.title()  #각 단어의 첫문자를 대문자로 변환

s = 'i like programming, i like swimming.'
print s.count('like')  #like의 등장 횟수 반환
print s.find('like')  #like의 첫 인덱스 반환
print s.find('programming')  #programming의 첫 인덱스 반환
print s.find('programmin')
print s.find('programmi')
print 
print s.find('like', 3)  #3인덱스부터 like의 인덱스를 찾아
print s.find('my')  #my라는 단어는 없어서 -1반환

print
print s.startswith('i like')  #i like로 시작하는 문자열인지 판단
print s.startswith('I like')  #대소문자 구별
print s.endswith('swimming.')  #swimming로 끝나는지 판단
print s.startswith('progr', 7)  #7번째 문자열이 progr로 시작하는지 판단
print

u = '    spam and ham           '
print u.strip()  #앞뒤 공백제거하여 새로운 스트링 생성
print u
y = u.strip()
print y
print 
print u.rstrip()  #오른쪽 공백제거
print u.lstrip()  #왼쪽 공북제거
print '     abc  '.strip()

print '><><abc<><><>'.strip('<>')  #<,>를 앞뒤에서 제거

p = '  \t abc \t '
print p
print p.strip()  #\t도 공백으로 인식되 제거

#u.replace(a,b): u안의 a문자를 b문자로 대치 
u = 'spam and ham'
print u.replace('spam', 'spam, egg')
print u

print
u = 'spam and ham   '
print u.split()  #공백으로 분리

print u.split('and')  #and로 분리
print

u2 = 'spam and ham\tegg\ncheese'
print u2.split()  #\t, \n도 공백으로 인식

#s.join(list). list 내부의 원소들을 s로 연결한 문자열 반환
t = u2.split()
print t
t2 = ':'.join(t)  #t의 원소들을 :로 연결
print type(t2)
print t2
print
t3 = ",".join(t)  #t의 원소들을 ,로 연결
print t3
print
t4 = '\n'.join(t)  #t의 원소들을 \n로 연결
print t4
print

u2 = u"스팸 햄 계란 치즈"
t2 = u2.split()
print t2
print t2[0], t2[1], t2[2], t2[3] 

lines = '''first lines
second line
third line'''
print type(lines)
lines2 = lines.splitlines()  #라인 기준으로 분리한 리스트 반환
print type(lines2)
print lines2

#align
u = 'spam and egg'
c = u.center(60)  #60자리를 확보하되, 기존 문자열을 가운데 정렬
print c
print u.ljust(60)  #60자리를 확보하되, 기존 문자열을 왼쪽 정렬
print u.rjust(60)  #60자리를 확보하되, 기존 문자열을 오른쪽 정렬

print u.center(60, '-')  #공백에 -문자를 채운다.
print u.ljust(60, '-')
print u.rjust(60, '-')

print '1234'.isdigit()  #문자열이 모두 숫자인가
print 'abcd'.isalpha()  #문자열이 모두 영문자인가
print '1abc234'.isalnum()  #문자열이 모두 영문자 또는 숫자인가
print 'abc'.islower()  #문자열이 모두 소문자인가
print 'ABC'.isupper()  #문자열이 모두 대문자인가
print '\t\r\n'.isspace()  #문자열이 모두 공백인가
print 'This Is A Title'.istitle()  #문자열의 첫글자가 대문자인가

s = '123'
print s.zfill(5)  #5자리 확보 후 문자열 쓰고, 남은 공백에 0채움
print 'goofy'.zfill(6)

#tupple formating
#포맷팅 문자: 문자열 내에 존재하는 %
#형식: 포맷팅 문자를 포함하는 문자열 % 튜플
print
print 'name = %s, age = %s' % ('gslee', '24')
letter = '''
hello %s, world!! '''

name = 'dong'
print letter % name
print
names = ['kim', 'dong', 'hee']
for name in names:
	print letter % name
	print '-' * 40

print "%s -- %s -- %d -- %f -- %e" % ((1,2), [3,4,5], 5, 5.3, 101.3)
print "%3d -- %5.2f -- %.2e" % (5, 5.356, 101.3)

a = 456
print '%d -- %o -- %x -- %X' % (a, a, a, a)

#dictionary formating
print
print '%(name)s -- %(phone)s' % {'name':'dong', 'phone':5235}
print '%(name)s -- %(phone)s' % {'phone':5235, 'name':'dong'}
print '%(name)s -- %(phone)s' % {'name':'dong', 'phone':5235, 'address':'seoul'}

# "1, 2, 3, 4, 5"와 같이 공백과 콤마 및 1부터 5까지의 숫자가 있는 문자열 s에서
# 숫자만 골라내어 리스트에 넣어 최종적으로는 숫자 1부터 5까지의 원소만 지니는
# 리스트 l을 출력하세요.
s = "1,2 ,3, 4, 5 "
parts = s.split(",")  # ","로 분리
l = []
for i in range(len(parts)):
	parts[i] = parts[i].strip()  #공백 제거
	l.append(parts[i])  #리스트에 삽입

print l

