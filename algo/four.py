#최소 공배수

num1 = int(input("input first number: "))
num2 = int(input("input second number: "))

t_num = 0

if num1 > num2:
    t_num = num1
else:
    t_num = num2

while t_num:
    if t_num % num1 == 0 and t_num % num2 == 0:
        print("최소공배수 %d" % t_num)
        break
    t_num += 1

