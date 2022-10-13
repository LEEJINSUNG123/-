import sys; sys.stdin = open("간단한소인수분해.txt")

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    div = [2,3,5,7,11]
    result = []
    for i in div:
        cnt = 0
        while N % i == 0:
            N = N / i
            cnt += 1
        result.append(cnt)
    print(f'#{tc}', end =" ")
    for j in range(5):
        print(result[j], end= ' ')
    print()


