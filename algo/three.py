#최대 공약수

num1 = int(input("input first number: "))
num2 = int(input("input second number: "))

t_num = 0

if num1 > num2:
    t_num = num2
else:
    t_num = num1

while t_num > 1:
    if num1 % t_num == 0 and num2 % t_num == 0:
        print("최대공약수 %d" % t_num)
        break
    t_num -= 1



