#문장에서 알파벳 갯수 카운트

string = str(input("input string; "))

alpha = str(input("input search alphabet: "))

count = 0
for i in string:
    if i == alpha:
        count += 1

print(count)