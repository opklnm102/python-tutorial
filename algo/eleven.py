#문장에 존재하는 중복되지 않는 알파벳 찾기

string = str(input("input string: "))

alphas = []
for i in string:
    exist = False
    for j in alphas:
        if i == j:
            exist = True
            break
    if not exist:
        alphas.append(i)

print(alphas)