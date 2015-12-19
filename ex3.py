import sys

## int
a = 23
b = 023
c = 0x23

print type(a), type(b), type(c)
print a, b, c

print sys.maxint  #max int range check

##float
a = 1.2
b = 3.5e3  #3.5 * 10^3 = 3500.0
c = -0.2e-4  #-0.2 * (1/10000) = -2 * (1/100000) = -2e-5

print type(a), type(b), type(c)
print a, b, c

##long
h1 = 122L
h2 = 2313232333333333333333333333333333

print type(h1), type(h2)
print h1, h2

##complex
a = 10 + 20j
print a
print type(a)

b = 10 + 5j
print b

print a + b

print
print abs(-3)
print int(3.141592)
print int(-3.1415)
print int(-3.9999)
print long(3)
print float(5)
print complex(3.4, 5)
print complex(6)
print divmod(5, 2)
print pow(2, 3)
print pow(2.3, 3.5)


##math
import math

print
print math.pi
print math.e
print math.sin(1.0)
print math.sqrt(2)

r = 5.0
a = math.pi * r * r
print a

degree = 60.0
rad = math.pi * degree / 180.0
print math.sin(rad), math.cos(rad), math.tan(rad)


##string
print 'Hello "World"'  #Hello "World"
print "Hello 'World'"  #Hello 'World'

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

s = "Hello World!"
print s[0]
print s[1]
print s[-1]
print s[-2]

print s[1:3]
print s[0:5]
print s[1:6:3]

print s[1:]
print s[:3]
print s[:]
print s[::2]
print s[::-1]

s = 'h' + s[1:]
print s

print 'Hello' + ' ' + 'World'
print 'Hello ' * 10
print '-' * 60

print len(s)

print 'World' in s
print 'World' not in s
print ' ' in s


