import sys; sys.stdin = open('컨테이너.txt')

t = int(input())
for tc in range(1, t+1):
    N, M = map(int,input().split())
    W = list(map(int, input().split()))
    T = list(map(int, input().split()))
    W.sort(reverse=True)
    T.sort(reverse=True)
    total = 0
    j = 0
    for i in range(len(W)):
        if j == len(T):
            break
        if T[j] >= W[i]:
            total += W[i]
            j += 1

    print(f'#{tc} {total}')