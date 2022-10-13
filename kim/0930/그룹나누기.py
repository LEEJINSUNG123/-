import sys; sys.stdin = open('그룹나누기.txt')

def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    p = list(range(N+1))     # make set

    for i in range(M):
        a = arr[2*i]
        b = arr[2*i + 1]
        p[find_set(b)] = find_set(a)

    cnt = 0
    for i in range(1, N+1):
        if p[i] == i:
            cnt += 1

    print(cnt)