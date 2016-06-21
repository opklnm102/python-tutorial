#비만도 측정

sex = 0
while not sex:
    sex = int(input("male is 1, female is 2: "))

height = int(input("input height: "))
weight = int(input("input weight: "))

s_weight = 0
if sex == 1:
    s_weight = (height - 100) * 0.9
else:
    s_weight = (height - 100) * 0.85

o_weight = weight / s_weight * 100

print("비만도 : %f" % o_weight)