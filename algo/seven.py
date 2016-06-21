#사각형 만들기

width = int(input("input width: "))
height = int(input("input height: "))

for i in range(0, height):
    p_str = ""
    for j in range(0, width):
        p_str += "*"
    print(p_str)

