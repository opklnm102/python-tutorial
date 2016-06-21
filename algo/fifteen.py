#단어 바꾸기, split()X

python =  "python is hard"
word = ""
list1 = []
for s in range(0, len(python)):
    if python[s] != ' ':
        word += python[s]
        if s == len(python) - 1:
            list1.append(word)
    elif python[s] == ' ':
        list1.append(word)
        word = ""

result = ""
for s in range(0, len(list1)):
    if list1[s] == "hard":
        list1[s] = "easy"
    if s != len(list1) - 1:
        result += list1[s] + ' '
    else:
        result += list1[s]

print(result)