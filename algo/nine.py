#직각삼각형2

length = int(input("input length: "))

for i in range(0, length):
    p_str = ""
    for j in range(0, length):
        if j >= length - (i + 1):
            p_str += "*"
        else:
            p_str += " "
    print(p_str)