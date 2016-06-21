#피보나치 수열

num = int(input("몇개의 피보나치 수열 항을 출력할까요? "))

fibo = [0, 1]
for idx in range(2, num):
    f1 = fibo[-2]  #뒤에서 2번째
    f2 = fibo[-1]  #뒤에서 1번째
    fibo.append(f1 + f2)  #더해서 리스트 뒤에 넣는다.

for f in fibo:
    print(f)