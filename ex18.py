# -*- coding: utf-8 -*-

#module import
#import는 코드를 가져오기만 하는 것이 아니라 가져온 코드를 수행

#1. import moduleName -> code run
#가장 기본적인 형태
#	이름공간 mymath가 그대로 유지되므로 mymath.area() 형태로 사용
#	모듈명.안에 존재하는 함수(인자)
import mymath
print mymath.area(5)

#2. from moduleName import names
#	해당 모듈에 존재하는 지정 이름들을 현재 이름 공간으로 불러들인다.
#	불러들인 각 이름들은 모듈 이름 없이 직접 사용 가능
#	import하는 이름들이 기존에 미리 존재하고 있었다면 그 이름들에 의해 참조되던 기존 객체들은 상실
mypi = 3.141592
from mymath import area, mypi
print area(5)
print mypi

#3. from moduleName import *
#	해당 모듈에 존재하는 '__'로 시작되는 이름들을 제외한 모든 이름들을 현재 이름 공간으로 불러들인다.
from mymath import *
print area(5)

#4. import moduleName as NewModuleName
#	해당 모듈을 새로운 다른 이름으로 사용하고자 할 때 사용
#	기존 모듈 이름이 너무 길거나 현재 사용중인 다른 이름들과 충돌이 일어날 때 유용
import string as chstr
print chstr
print
print chstr.punctuation

#5. from moduleName import name as newName[, name as NewName]
#	해당 모듈 내에 정의된 이름을 다른 새로운 이름으로 사용하고자 할 때 사용
from string import replace as substitute
print substitute
print substitute('ham chicken spam', 'chicken', 'egg')

from string import replace as substitute, upper as up
print up
print up('abc')

#import문은 보통의 문(statement)이 작성될 수 있는 곳이라면 어디에서나 사용 가능
#	함수 정의 def문 안이나 if문 안에서 사용가능
def str_test(s):
	import string
	t = string.split(s)
	print t

str_test('ha ha haa')

#import mymath를 수행할 때 발생하는 일
#	1. mymath.pyc를 찾는다
#	2. 없다면 mymath.py를 찾아서 mymath.pyc를 생성
#	3. 생성된 mymath.pyc를 메모리로 읽어들여 수행
#.pyc 파일
#	바이트 코드 파일
#		기계나 플랫폼(OS)에 의존하지 않도록 만들어진 일종의 Object Code
#		파이썬은 컴파일 언어이면서 동시에 인터프리터 언어의 수행 방식을 취하고 있다.
#새로운 .pyc 생성에 대한 판단
#	.py수정시간이 .pyc 수정시간보다 더 최근일 때
#.py가 없이도 .pyc만 있어도 import가능
#	코드를 숨기는 간단한 기법으로 활용

#모듈 이름과 이미 사용하고 있던 이름이 같다면?
#이전의 이름이 참조하던 객체는 상실
string = "My first string"
import string
print string

#한번 import된 모듈은 메모리에 적재, 나중에 동일 모듈 import시 메모리에 적대된 모듈이 즉시 사용
import string
string.a = 1
string = "My first string"
print string

import string
print string.a  #string모듈이 기존에 이미 등록되었던 것임을 알 수 있다.


#__name__
#	현재의 모듈이 최상위 모듈로서 수행되는지, 아니면 다른 모듈에 의해 import되어 수행되는지를 구별하기 위해 주로 사용
#prname.py를 직접 수행할 때의 출력 내용: __main__
#	prname.py가 최상위 모듈로서 수행됨을 의미		
#prname.py가 모듈로서 다른 이름 공간으로 import되어질 떄 출력 내용: prname
import prname
print prname.__name__

#모듈이름과 동일한 이름 출력
import string
print string.__name__  #string

import re
print re.__name__  #re

import mimetools
print mimetools.__name__  #mimetools

import os
print os.__name__  #is

print __name__

#보통 파이썬 모듈을 개발할 때에는 마지막 부분에 if __name__ == "__main__": 과 같은 코드를 추가하여 테스트 코드를 삽입
#file: module_test.py
def add(a, b):
	return a + b

def f():
	print "Python is becoming popular"

if __name__ == "__main__":  #test 가능
	print add(1, 10)
	f()

#아래 코드는 최상위 모듈로서 수행될 때에만 test() 호출이 일어난다.
import module_test

print module_test.add(10, 20)

#Package
#	여러 모듈들을 한데 묶어서 정리해 놓은 구조
#	물리적으로 여러 모듈 파일을 모아 놓은 디렉토리에 해당
#		최상위 디렉토리 이름이 패키지 이름이 된다.
#		최상위 디렉토리 하위에 여러 서브 디렉토리는 해당 최상위 패키지의 하위 패키지가 된다.
#__init__.py: 디렉토리는 패키지로 인식시키는 역할

#package import
import pack1.HMM
pack1.HMM.train()

#package module import
from pack1 import HMM
HMM.train()

from pack1.HMM import train
train()

from pack1.HMM import *
train()
loadModel()
saveModel()

