#팩토리얼

number = 0
while not (number < 11 and number > 0):
    number = int(input("input number(0~10): "))

result = 1
for i in range(1, number + 1):
    result *= i

print(result)