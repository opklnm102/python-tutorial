#문장에서 존재하는 알파벳 카운트

string = str(input("input string: "))

alphas = {}
for i in string:
    exist = False
    for j in alphas.keys():
        if i == j:
            exist = True
            alphas[j] += 1
            break
    if not exist:
        alphas[i] = 1

print(alphas)