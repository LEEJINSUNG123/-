import sys; sys.stdin = open('미로의거리.txt')

di = [-1, 1, 0, 0]
dj = [0, 0,-1, 1]

def bfs2(x,y):
    Q = []
    Q.append((x, y))
    visited[x][y] = 1

    while Q:
        x, y = Q.pop(0)
        if arr[nx][ny] == 3:
            return visited[x][y] - 2

        for i in range(4):
            nx = x + di[i]
            ny = y + dj[i]
            if 0 <= nx < N and 0 <= ny < N:
                # if arr[nx][ny] == 3:
                #     return visited = [x][y]
                if arr[nx][ny] == 0 and visited[nx][ny] == 0:
                    Q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
    return 0


def bfs(x,y):
    global flag
    q = []
    q.append([x, y])
    arr[x][y] = 1

    while q:
        v = q.pop(0)
        for i in range(4):
            ni = v[0] + di[i]
            nj = v[1] + dj[i]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 'x':
                    flag = 1
                    return arr[v[0]][v[1]] - 1
                if not arr[ni][nj]:
                    q.append([ni, nj])
                    arr[ni][nj] = arr[v[0]][v[1]] + 1
    return 0

def find_start_end(arr, N):
    global sx, sy, ex, ey
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                sx, sy = i, j
            elif arr[i][j] == 3:
                ex, ey = i, j

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    sx = sy = ex = ey = 0
    find_start_end(arr, N)
    arr[ex][ey] = 'x'
    flag = 0
    x = bfs(sx,sy)

    if flag:
        print(f'#{tc} {x}')
    else:
        print(f'#{tc} 0')


