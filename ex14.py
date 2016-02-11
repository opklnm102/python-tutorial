# -*- coding: utf-8 -*-

import os  #파일을 다루는 다양한 메소드 존재

#os.listdir('path'): 디렉토리 안에 들어있는 각 파일 목록을 리스트로 반환
print os.listdir('.')  #current directory
print

print os.listdir('../')  #parent directory

#os.path.isfile(path): 순수파일이면 True
#os.path.isdir(path): 디렉토리면 True
#os.path.islink(path): 심볼릭링크면 True
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

#파일의 권한
#os.access(filepath, mode)
#	mode에 들어갈 값
#		os.F_OK: 파일 자체가 존재하는 것을 테스트
#		os.R_OK: 읽기 권한이 있는 것을 테스트
#		os.W_OK: 쓰기 권한이 있는 것을 테스트
#		os.X_OK: 실행 권한이 있는 것(또는 디렉토리인지)을 테스트

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

#파일 권한 변경
#os.chmod(path, mode)
os.chmod('t.txt', 0664)  #linux chmod와 같다.

#file rename
#os.rename(old_filepath, new_filepath)
os.rename('t.txt', 't.txt')  #file rename
print os.access('t.txt', os.F_OK)
print os.access('t1.txt', os.F_OK)

#file move
#os.rename(old_filepath, new_filepath)
os.rename('t1.txt', 'a/t1.txt')  #file move
print os.access('t1.txt', os.F_OK)

#file copy
#shutil.copyfile(src_filepath, dest_filepath)
import shutil

shutil.copyfile('t.txt','t1.txt')
print os.access('t.txt', os.F_OK)

#파일 이름 다루기
#1. absolute path로 변환
#os.path.abspath(상대경로)
print os.path.abspath('o.txt')  #파일 존재유무에 관계없이 절대경로 리턴

#2. 주어진 경로의 파일이 존재하는지 확인
f = '/home/dong/Dev/python/python-tutorial/t.txt'
print os.path.exists(f)
print os.path.exists('sample.txt')

#3. 현재/부모 디렉토리를 가리키는 이름 얻기
print os.curdir  #current directory
print os.pardir  #parent directory

#4. 디렉토리 분리 문자 얻기
print os.sep  #separation. /

#경로명 분리하기
#1. 경로와 파일명으로 분리
f = '/home/dong/Dev/python/python-tutorial/t.txt'

print os.path.basename(f)  #file name 추출
print os.path.dirname(f)  #directory path 추출

#2. 경로명과 파일명을 한번에 분리. 튜플로
print os.path.split(f)  #return tuple ('directory path','file name')

#3. MS 윈로우즈에서 드라이브명과 파일 경로명 분리
print os.path.splitdrive(f)  #윈도우에서 드라이브명 확인

#4. 확장자 분리
print os.path.splitext(f)  #('directory path','extension')

#디렉토리에 관련된 일반 작업
#1. 현재 작업 디렉토리 알아보기
print os.getcwd()  #current working directory

#2. 작업 디렉토리 변경하기
os.chdir('/home/dong/Dev/python/')
print os.getcwd()
os.chdir('/home/dong/Dev/python/python-tutorial/')

#3. directory create
os.mkdir('temp')  #0755(rwxr-xr-x) 기본모드 , File exists -> error
os.mkdir('temp2', 0700)  #0700(rwx------), File exists -> error
os.makedirs('temp/level1/level2')  #0755 기본모드, 중간에 필요한 디렉토리 생성(재귀적), File exists -> error

print os.access('/home/dong/Dev/python/python-tutorial/temp', os.F_OK)
print os.access('/home/dong/Dev/python/python-tutorial/temp2', os.F_OK)
print os.access('/home/dong/Dev/python/python-tutorial/temp/level1/level2', os.F_OK)

#4. directory delete
os.rmdir('temp2')  #directory에 내용이 없을 때 삭제 가능
os.rmdir('temp')  #directory에 다른 파일이 있으면 삭제x. OS error 발생

#5. 다단계 디렉토리 삭제
#os.removedirs(filepath)
#	filepath에 지정된 디렉토리들 중 맨 오르쪽 디렉토리부터 차례차례로 삭제
#	디렉토리에 다른 파일이 있으면 삭제하지 않고 중단
os.removedirs('temp/level1/level2')  # <-> makedirs()

#6.하위 디렉토리까지 모두 한번에 삭제
shutil.rmtree('temp')  #조심해서 사용

#7. directory copy
#shutil.copytree(src_filepath, dest_filepath)
#	하위 디렉토리와 파일등을 지니고 있는 디렉토리를 복사
os.mkdir('temp')
os.mkdir('temp/temp2', 0700)
shutil.copytree('temp', 'myweb_backup')

#directory search
#os.walk(filepath)
#	filepath부터 시작하여 재귀적으로 모든 사위 디렉토리까지 탐색하는 함수
#	탐색시 발견하는 모든 파일에 대해서 튜플 리턴
#		(dirpath, dirnames, filenames)
#			dirpath: 탐색하고 있는 디렉토리 경로
#			dirnames: dirpath안에 존재하는 서브 디렉토리 리스트
#			filenames: dirpath안에 존재하는 파일리스트
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

