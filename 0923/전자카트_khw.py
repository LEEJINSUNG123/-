import sys; sys.stdin = open('전자카트.txt')

def perm(n, k, ssum):
    global ans
    if ans < ssum:
        return

    if n == k:
        ssum += arr[t[N-1]][t[N]]
        if ans > ssum:
            ans = ssum
    else:
        for i in range(n):
            if visited[i]: continue
            visited[i] = 1
            t[k] = i
            perm(n, k+1, ssum + arr[t[k-1]][t[k]])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    t = [0] * N + [0]   # 0 1 2 0 (출발과 도착을 고정)
    visited = [0] * N
    visited[0] = 1      # 0번은 제외하겠다.
    ans = 987654321
    perm(N, 1, 0)          # k = 0 는 제외
    print(f'#{tc} {ans}')