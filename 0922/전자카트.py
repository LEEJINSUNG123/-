import sys; sys.stdin = open('전자카트.txt')
# nPn
def perm(n, k, arr):  # k는 깊이
    global total, min_v
    if n == k:
        for i in range(k):
            total += arr[p[i]][p[i+1]]
        if total < min_v:
            min_v = total
        total = 0
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                p[k] = a[i]
                perm(n, k+1, arr)
                visited[i] = 0

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    a = [i for i in range(1, N+1)]
    arr = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    p = [0] * (N+1)
    p[0] = p[N] = a[0]
    visited = [0] * N
    visited[0] = 1
    total = 0
    min_v = 987654321
    perm(N, 1, arr)
    print(f'#{tc} {min_v}')
