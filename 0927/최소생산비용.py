import sys; sys.stdin = open('최소생산비용.txt')

def dfs(x, y, ssum):
    global ans
    if ans <= ssum:
        return
    if x == N:
        if ans > ssum:
            ans = ssum
        return
    else:
        for j in range(N):
            if not visited[j]:
                visited[j] = 1
                dfs(x+1, j, ssum + arr[x][j])
                visited[j] = 0


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 987654321
    visited = [0] * N

    dfs(0, 0, 0)
    print(f'#{tc} {ans}')
