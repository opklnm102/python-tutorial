#sort

#selection sort
# 탐색의 시작위치를 1씩 증가시키면서 요소 중 최소값을 가장 앞의 요소랑 swap
list1 = [4, 2, 3, 8, 7, 1]
for i in range(0, len(list1)):
    min_idx = i
    for j in range(i+1, len(list1)):
        if list1[min_idx] > list1[j]:
            min_idx = j
    list1[min_idx], list1[i] = list1[i], list1[min_idx]

print(list1)

#bubble sort
# 바로 옆의 것과 비교
list1 = [4, 2, 3, 8, 7, 1]
for i in range(0, len(list1)):
    for j in range(0, len(list1) - 1):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]

print(list1)

#insert sort
#정렬된 리스트에 정렬할 요소를 삽입
list1 = [4, 2, 3, 8, 7, 1]
for i in range(1, len(list1)):
    j = i - 1
    val = list1[i]
    while list1[j] > val and j>=0:
        list1[j+1] = list1[j]
        j -= 1
    list1[j+1] = val

print(list1)



