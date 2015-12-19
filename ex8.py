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















