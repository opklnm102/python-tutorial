
# os module - OS의 기능들을 사용할 수 있는 모듈

import os

print(os)

# getcwd() - 현재 작업중인 디렉토리를 보여줌
cwd = os.getcwd()
print(cwd)

# chdir() - 현재 작업 디렉토리를 변경
os.chdir("/home/dong/Dev/python/python-tutorial")

# listdir() - 입력한 경로의 파일과 폴더 목록을 리스트로 반환
for file_name in os.listdir(cwd):
    print(file_name)

# mkdir() - 폴더 생성
os.mkdir(cwd + "/test1")

# makedirs() - 폴더 생성(하위폴더 포함). mkdir -p와 동일
os.makedirs(cwd + "/test2/test3/test4/test5")

# remove(), unlink() - 파일 삭제
# os.remove(cwd + "/test")

# rmdir(), removedirs() - 폴더 삭제
os.rmdir(cwd + "/test1")  # 내용이 있을 경우 오류(비어있어야 함)
os.removedirs(cwd + "/test2/test3/test4/test5")  # 가장안에 있는 폴더 1개씩 삭제

# os.path 모듈 - 파일, 폴더에 대한 정보를 알 수 있다.
# 생성시간, 접근권한, 파일존재 유무 판단 등
# isdir() - 폴더 유무 판단
print("isdir() - " + str(os.path.isdir(cwd)))

# isfile() - 파일 유무 판단
print("isfile() - " + str(os.path.isfile(cwd)))

# exists() - 파일이나 폴더가 존재하는지 판단
print("exists() - " + str(os.path.exists(cwd)))

# getsize() - 파일의 크기(Byte)를 반환
print("getsize() - " + str(os.path.getsize(cwd)))

# split(), splitext() - 파일과 폴더의 경로 구분(튜플 반환)
# ex) image태그의 img url에서 이미지 파일의 경로와 이름을 분리할 때 사용
print(os.path.split(cwd))  #마지막 폴더 분리
print(os.path.splitext(cwd))  #확장자 분리

# join() - 파일 이름과 폴더 이름을 합친다.
join_1 = os.path.split(cwd)
print(join_1)

print(os.path.join(join_1[0], join_1[1]))

# dirname() - 완성경로의 폴더경로만 꺼낸다.
print(os.path.dirname(cwd))

# basename() - 파일 이름만 꺼낸다.
print(os.path.basename(cwd))

# 파일 생성 및 수정하기
# 쓰기 모드
f = open("test.txt", "w")
print(f.write("test txt file"))  # cwd에 생성됨. 글자수 반환

f.close()

# 매번 파일을 열고 닫는것이 귀찮을 경우 파일관리를 하는 콘텍스트 매니저 사용
# 자동으로 열고 닫고 수행
with open("test.txt", "a") as test:
    test.write("\n with test\n")

# 읽기 모드
# readline() - 한줄씩 읽기
f = open("t.txt", "r")
print(f.readline())
print(f.readline())
f.close()

# readlines() - 한꺼번에 여러줄 읽어서 출력
f = open("t.txt", "r")
for food in f.readlines():
    print(food)
f.close()

# file pointer - 파일에서 현재 어디까지 읽었는지 위치 관리
# tell() - 현재 파일 포인터의 위치
f = open("t.txt", "r")
f.readline()
print(f.tell())
f.readline()
print(f.tell())

# seek() - 지정 위치로 파일 포인터 이동
f.seek(0)
print(f.tell())

# 바이너리 모드
# ex) image copy
t = open("t.txt", "rb")
t2 = open("t2.txt", "wb")
t2.write(t.read())  # t를 t2에 copy
t.close()
t2.close()







