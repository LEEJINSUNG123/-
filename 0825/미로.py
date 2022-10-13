import sys; sys.stdin = open("미로.txt")

def dfs(x,y):
    global flag
    # 방문체크
    if arr[x][y] == 3:
        flag = 1
        return
    visited[x][y] = 1

    # 인접한 정정미 방문 안했으면 dfs
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 인덱스체크 방문체크 벽체크
        if nx < 0 or nx == N: continue
        if ny < 0 or ny == N: continue
        if visited[nx][ny] == 1: continue
        if arr[nx][ny] == 1: continue
        dfs(nx, ny)

'''
def
'''

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    flag = 0
    arr = [list(map(int,input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    # def find_start(arr)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                x = i
                y = j
                # return i, j
    # sx, sy = find_start(arr)
    dfs(x,y)
    print(f'#{tc} {flag}')
