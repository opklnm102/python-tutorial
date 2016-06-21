#2개의 숫자 중 큰수-작은수 출력

n1 = int(input("첫번째 수 입력: "))
n2 = int(input("두번째 수 입력: "))

if n1 > n2:
    print(n1 - n2)
else:
    print(n2 - n1)