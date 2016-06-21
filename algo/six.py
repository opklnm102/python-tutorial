#숫자 중에서 큰값, 작은값 찾기
#max(), min() 사용X

list1 = [12, 42, 32, 51, 23, 25, 22]
max = list1[0]
min = list1[0]

for item in list1:
    if item > max:
        max = item
    if item < min:
        min = item

print(max)
print(min)