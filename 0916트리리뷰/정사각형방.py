import sys; sys.stdin = open('정사각형방.txt')

def bfs(x,y):
    Q = []
    Q.append((x, y))
    start = arr[x][y]
    cnt = 1

    while Q:
        x, y = Q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == arr[x][y] + 1:
                    Q.append((nx, ny))
                    cnt += 1
                    break
    return start, cnt


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        for j in range(N):
            start, cnt = bfs(i, j)
            if max_v < cnt:
                max_v = cnt
                max_idx = start
            elif max_v == cnt:
                if max_idx > start:
                    max_idx = start

    print(f'#{tc} {max_idx} {max_v}')