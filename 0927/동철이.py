import sys; sys.stdin = open('동철이.txt')

def dfs(k, per):
    global ans

    if ans >= per * 100:
        return
    if k == N:
        per *= 100
        if ans < per:
            ans = per
        return

    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                dfs(k+1, per * P[k][i] * 0.01)
                visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 0
    dfs(0, 1)
    print(f'#{tc} {ans:.6f}')


