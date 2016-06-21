#단어 바꾸기, split() O

python =  "python is hard"

list1 = python.split(" ")
result = ""
for s in range(0, len(list1)):
    if list1[s] == "hard":
        list1[s] = "easy"
    if s != len(list1) - 1:
        result += list1[s] + ' '
    else:
        result += list1[s]

print(result)
