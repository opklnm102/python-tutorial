# -*- coding: utf-8 -*-

import os

#
print os.listdir('.')  #current directory
print

print os.listdir('../')  #parent directory

#
def filetype(fpath):
	print fpath, ':',
	if os.path.isfile(fpath):
		print 'Regular file'
	if os.path.isdir(fpath):
		print 'Directory'
	if os.path.islink(fpath):
		print 'Symbolic link'

flist = os.listdir('.')
for fname in flist:
	filetype(fname)

#
def fileaccess(fpath):
	print fpath, ':',
	if os.access(fpath, os.F_OK):
		print 'Exists',
	else:
		return
	if os.access(fpath, os.R_OK):
		print 'R',
	if os.access(fpath, os.W_OK):
		print 'W',
	if os.access(fpath, os.X_OK):
		print 'X',
	print

flist = os.listdir('.')
for fname in flist:
	fileaccess(fname)

#
os.chmod('t.txt', 0664)  #linux chmod와 같다.

#file rename
os.rename('t.txt', 't.txt')  #file rename
print os.access('t.txt', os.F_OK)
print os.access('t1.txt', os.F_OK)

#file move
# os.rename('t1.txt', 'a/t1.txt')  #file move
print os.access('t1.txt', os.F_OK)

#file copy

import shutil

shutil.copyfile('t.txt','t1.txt')
print os.access('t.txt', os.F_OK)

#
#1. absolute path
print os.path.abspath('o.txt')  #파일 존재유무에 관계없이 절대경로 리턴

#2. 
f = '/home/dong/Dev/python/python-tutorial/t.txt'
print os.path.exists(f)
print os.path.exists('sample.txt')

#3. 
print os.curdir  #current directory
print os.pardir  #parent directory

#4.
print os.sep  #separation

#
#1.
f = '/home/dong/Dev/python/python-tutorial/t.txt'

print os.path.basename(f)  #file name
print os.path.dirname(f)  #directory path

#2.
print os.path.split(f)  #return tuple ('directory path','file name')

#3.
print os.path.splitdrive(f)

#4.
print os.path.splitext(f)  #('directory path','extension')

#
#1.  
print os.getcwd()  #current working directory

#2.
os.chdir('/home/dong/Dev/python/')
print os.getcwd()
os.chdir('/home/dong/Dev/python/python-tutorial/')

#3. directory create
#os.mkdir('temp')  #0755(rwxr-xr-x) 기본모드 , File exists -> error
#os.mkdir('temp2', 0700)  #0700(rwx------), File exists -> error
#os.makedirs('temp/level1/level2')  #0755 기본모드, 중간에 필요한 디렉토리 생성, File exists -> error

print os.access('/home/dong/Dev/python/python-tutorial/temp', os.F_OK)
print os.access('/home/dong/Dev/python/python-tutorial/temp2', os.F_OK)
print os.access('/home/dong/Dev/python/python-tutorial/temp/level1/level2', os.F_OK)

#4. directory delete
# os.rmdir('temp2')  #directory에 내용이 없을 때 삭제 가능
# os.rmdir('temp')  #directory에 다른 파일이 있으면 삭제x

#5.
#os.removedirs('temp/level1/level2')  #

#6.
#shutil.rmtree('temp')

#7. directory copy
#os.mkdir('temp')
#os.mkdir('temp/temp2', 0700)
#shutil.copytree('temp', 'myweb_backup')

#directory search
for path, subdirs, files in os.walk(os.getcwd()):
	for fname in files:
		if fname.endswith('.ttt'):
			fullpath = os.path.join(path, fname)
			print 'removing', fullpath
			os.remove(fullpath)

#리눅스를 기준으로 root('/')로 부터 모든 하위 디렉토리들을 재귀적으로 방문하면서
#'.py'를 확장자로 지닌 각각의 파일들에 대한 전체 경로를 출력

import os

for path, subdirs, files in os.walk('/'):
	for fname in files:
		if fname.endswith('.py'):
			fullpath = os.path.join(path, fname)
			print fullpath

for path, subdirs, files in os.walk('/'):
	for fname in files:
		if os.path.splitext(fname)[1] == '.py':
			fullpath = os.path.join(path, fname)
			print fullpath

