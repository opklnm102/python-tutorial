
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
























