# -*- coding: utf-8 -*-

s = 'i like programming.'
print s.upper()
print s.upper().lower()
print 'I Like Programming'.swapcase()
print s.capitalize()
print s.title()

s = 'i like programming, i like swimming.'
print s.count('like')
print s.find('like')
print s.find('programming')
print s.find('programmin')
print s.find('programmi')
print 
print s.find('like', 3)
print s.find('my')

print
print s.startswith('i like')
print s.startswith('I like')
print s.endswith('swimming.')
print s.startswith('progr', 7)
print

u = '    spam and ham           '
print u.strip()
print u
y = u.strip()
print y
print 
print u.rstrip()
print u.lstrip()
print '     abc  '.strip()

print '><><abc<><><>'.strip('<>')

p = '  \t abc \t '
print p
print p.strip()

u = 'spam and ham'
print u.replace('spam', 'spam, egg')
print u

print
u = 'spam and ham   '
print u.split()

print u.split('and')
print

u2 = 'spam and ham\tegg\ncheese'
print u2.split()

t = u2.split()
print t
t2 = ':'.join(t)
print type(t2)
print t2
print
t3 = ",".join(t)
print t3
print
t4 = '\n'.join(t)
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
lines2 = lines.splitlines()
print type(lines2)
print lines2

#align
u = 'spam and egg'
c = u.center(60)
print c
print u.ljust(60)
print u.rjust(60)

print u.center(60, '-')
print u.ljust(60, '-')
print u.rjust(60, '-')

print '1234'.isdigit()
print 'abcd'.isalpha()
print '1abc234'.isalnum()
print 'abc'.islower()
print 'ABC'.isupper()
print '\t\r\n'.isspace()
print 'This Is A Title'.istitle()

s = '123'
print s.zfill(5)
print 'goofy'.zfill(6)

#tupple formating
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

