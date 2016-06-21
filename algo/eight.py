#직각 삼각형

length = int(input("input length: "))

for i in range(0, length):
    p_str = ""
    for j in range(0, i + 1):
        p_str += "*"
    print(p_str)