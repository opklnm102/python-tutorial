# -*- coding: utf-8 -*-

#module import
#1. import moduleName -> code run
import mymath
print mymath.area(5)

#2. from moduleName import names
mypi = 3.141592
from mymath import area, mypi
print area(5)
print mypi

#3. from moduleName import *
from mymath import *
print area(5)

#4. import moduleName as NewModuleName
import string as chstr
print chstr
print
print chstr.punctuation

#5. from moduleName import name as newName[, name as NewName]
from string import replace as substitute
print substitute
print substitute('ham chicken spam', 'chicken', 'egg')

from string import replace as substitute, upper as up
print up
print up('abc')

#
def str_test(s):
	import string
	t = string.split(s)
	print t

str_test('ha ha haa')

#
string = "My first string"
import string
print string

#
import string
string.a = 1
string = "My first string"
print string

import string
print string.a


#
import prname
print prname.__name__

import string
print string.__name__

import re
print re.__name__

import mimetools
print mimetools.__name__

import os
print os.__name__

print __name__

#
import module_test

print module_test.add(10, 20)

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

