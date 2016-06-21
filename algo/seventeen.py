#초를 시, 분, 초로

number = int(input("input seconds: "))

sec = number % 60
number /= 60

min = number % 60
number /= 60

hour = number

print("%d : %d : %d" % (hour, min, sec))