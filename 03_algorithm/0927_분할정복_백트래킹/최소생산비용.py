import sys; sys.stdin = open('최소생산비용_input.txt')
def perm(n, k, ssum):
    global ans
    if ans <= ssum: return

    if n == k:
        if ans > ssum:
            ans = ssum
    else:
        for i in range(n):
            if visited[i]: continue
            visited[i] = 1
            p[k] = a[i]
            perm(n, k+1, ssum + arr[k][a[i]])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    a = list(range(N))
    p = [0] * N
    visited = [0] * N
    ans = 987654321
    perm(N, 0, 0)
    print(f'#{tc} {ans}')