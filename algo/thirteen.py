#리스트 정렬하기

numbers = []

while not len(numbers) == 5:
    t_n = int(input("input number: "))
    numbers.append(t_n)

for n in range(0, len(numbers)):
    for t_n in range(0, len(numbers)):
        if numbers[n] < numbers[t_n]:
            tmp = numbers[t_n]
            numbers[t_n] = numbers[n]
            numbers[n] = tmp

print(numbers)