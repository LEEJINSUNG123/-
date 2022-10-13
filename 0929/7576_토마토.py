import sys; sys.stdin = open('7576_토마토.txt')


def bfs(t):
    global cnt
    q = []
    q.extend(t)

    while q:
        for _ in range(len(q)):
            x, y = q.pop(0)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                    q.append((nx, ny))
                    arr[nx][ny] = 1
        cnt += 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 가로, 세로
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
tomato = []
# -1 빈칸, 0 익지 않은 토마토, 1 익은 토마토
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            tomato.append((i, j))

bfs(tomato)
count = 0
for i in range(N):
    count += arr[i].count(0)
if count > 0:
    print(-1)
else:
    print(cnt-1)