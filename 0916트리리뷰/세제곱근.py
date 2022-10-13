import sys; sys.stdin = open('세제곱근.txt')

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    k = int(N**(1/3))
    q = N**(1/3)
    print(q)
    print(round(q, 2))
    c = [k, k-1, k+1]
    for i in c:
        if i ** 3 == N:
            print(f'#{tc} {i}')
            break
        elif i == k+1:
            print(f'#{tc} -1')


