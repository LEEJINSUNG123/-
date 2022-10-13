import sys; sys.stdin = open('격자판이어붙이기_input.txt')
def dfs(x, y, k, num):
    # global ans
    if k == 6:
        # if visited[num] != tc:
        #     ans += 1
        #     visited[num] = tc
        t.add(num)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4:
                dfs(nx, ny, k+1, num * 10 + arr[nx][ny])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# visited = [0] * 10000000  # 0 ~ 9999999
T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    t = set()
    # ans = 0
    for i in range(4):
        for j in range(4):
            dfs(i, j, 0, arr[i][j])

    print(f'#{tc} {len(t)}')