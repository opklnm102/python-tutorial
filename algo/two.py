#약수 구하기

num = int(input("1이상의 숫자를 입력: "))

divisors = []
t_num = int(num/2)  #약수는 자기 자신을 반을 나눈것을 넘지 않는다. 홀수를 대비해 int로 소수점 없앤다.

while t_num > 1:  #t_num을 1씩 감소시키면서 나누어떨어지는지 확인
    if num % t_num == 0:
        divisors.append(t_num)
    t_num -= 1

print(divisors)