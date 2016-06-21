#리스트에서 원하는 값 찾기

numbers = [2, 15, 25, 32, 54, 32]

find_number = int(input("input number: "))

idx = -1
for i in range(0, len(numbers)):
    if numbers[i] == find_number:
        idx = i

if idx == -1:
    print("fail")
else:
    print("%d" % idx)
