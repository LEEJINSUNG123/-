import sys; sys.stdin = open("가빠문타.txt", "r")

t = int(input())

for tc in range(1, t+1):
    a, b = input().split()
    m = len(a)
    n = len(b)

    i = cnt = 0

    while i < m-n+1: # =3
        s = ''
        for j in range(n):
            s += a[i+j]
        if s == b:
            cnt += 1
            i += n
        else:
            i += 1
    print(f'#{tc} {m-(cnt*n)+cnt}')