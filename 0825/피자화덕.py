import sys; sys.stdin = open('피자화덕.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    count = [0] * M
    pizza = []
    for i in range(N):
        pizza.append(C[i])
    # print(pizza)
    for x, y in enumerate(C):
        print(x,y)
    for j in range(10):
        x = pizza.pop(0) // 2
        if x == 0 and len(C) > 0:
            pizza.append(C[0])
        else:
            pizza.append(x)
        print(pizza)
