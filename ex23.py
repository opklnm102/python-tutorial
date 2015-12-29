# -*- coding: utf-8 -*-

#NameError
#4 + spam * 3

#ZeroDivisionError
def division():
	for n in range(0, 5):
		print 10.0 / n

#division()


#TypeError
#'2' + 2


#IndexError
l = [1, 2]
#print l[2]


#KeyError
d = {'a': 1, 'b': 2}
#print d['c']

#IOError
#a = open('aaa.txt')

try:
	print 1.0 / 0.0
except ZeroDivisionError:
	print 'zero division error!!!'

def division():
	for n in range(0, 5):
		try:
			print 10.0 / n
		except ZeroDivisionError, msg:
			print msg
		else:
			print "Success"
		finally:
			print "finally"

division()

try:
	spam()
except NameError, msg:  # == NameError as msg
	print "Error - ", msg


def zero_division():
	x = 1 / 0

try:
	zero_division()
except ZeroDivisionError, msg:
	print "Zero division error!!! - ", msg


#all except catch
print
try:
	spam()
	print 1.0 / 0.0
except:
	print 'Error'


#multiple except
print
b = 0.0
name = 'aaa.txt'
try:
	print 1.0 / b  #ZeroDivisionError
	spam()  #NameError
	f = open(name, 'r')  #IOError
	'2' + 2  #TypeError
except NameError:
	print "NameError!!!"
except ZeroDivisionError:
	print "ZeroDivisionError!!!"
except TypeError, IOError:  #tuple
	print "TypeError or IOError!!!"
else:
	print "No Exception!!!"
finally:
	print "Exit!!!"

#best error catch
print
import os
print os.getcwd()
filename = "aaa.txt"

try:
	f = open(filename, 'r')
except IOError, msg:
	print msg
else:
	a = float(f.readline())
	try:
		answer = 1.0 / a
	except ZeroDivisionError, msg:
		print msg
	else:
		print answer
	finally:
		print "finally!!!"
		f.close()


#same error catch
print
def dosomething():
	a = 1 / 0

try:
	dosomething()
except ArithmeticError:
	print "ArithmeticException occured"

try:
	dosomething()
except ZeroDivisionError:  #ZeroDivisionError
	print "ZeroDivisionError occured"
except ArithmeticError:  #FloatingPotinError
	print "ArithmeticException occured"


try:
	dosomething()
except ArithmeticError:  #FloatingPotinError
	print "ArithmeticException occured"
except ZeroDivisionError:  #ZeroDivisionError
	print "ZeroDivisionError occured"


#raise -> except occured
class SquareSeq:
	def __init__(self, n):
		self.n = n
	def __getitem__(self, k):  #indexing matching
		if k >= self.n or k < 0:
			raise IndexError  #
		return k * k
	def __len__(self):
		return self.n

s = SquareSeq(10)
print s[2], s[4]
for x in s:  #IndexError
	print x,
try:
	print s[20]  #IndexError occured
except IndexError:
	print "IndexError!!!"

class Big(Exception):
	pass

class Small(Big):
	pass

def dosomething1():
	x = Big()
	raise x

def dosomething2():
	raise Small()

for f in (dosomething1, dosomething2):
	try:
		f()
	except Big:
		print "Exception occurs!!!"

#except mag passing
def f():
	raise Exception, "message!!!"

try:
	f()
except Exception, a:
	print a

a = 10
b = 0
try:
	if b == 0:
		raise ArithmeticError("division by zeor")
	a / b
except ArithmeticError, v:
	print v

#t.txt 파일에서 숫자를 읽어서 실수로 변환한 후 나누기 연산을 수행
#여기서 발생할 수 있는 예외를 처리
filename = "ttt.txt"
try:
	f = open(filename, 'r')
except IOError, msg:
	print msg
else:
	a = float(f.readline())
	try:
		answer = 1.0 / a
	except ZeroDivisionError, msg:
		print msg
	else:
		print answer
	finally:
		print "- end -"
		f.close()
