import sys; sys.stdin = open('최소합.txt')

def dfs(x, y):
    global total, min_v
    # 방문체크
    visited[x][y] = 1
    total += arr[x][y]

    if x == N-1 and y == N-1:
        if total < min_v:
            min_v = total
        return

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        # if nx == N-1 and ny == N-1:
        #     dfs(nx, ny)
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            dfs(nx, ny)

def bfs(x, y):
    Q = []
    Q.append((x, y))
    visited[x][y] = arr[x][y]

    while Q:
        x, y = Q.pop(0)

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N :  # 인덱스 체크
                if visited[nx][ny] == 0:
                    Q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + arr[nx][ny]
                else:
                    if visited[x][y] + arr[nx][ny] <= visited[nx][ny]:
                        Q.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + arr[nx][ny]
                    elif visited[x][y] + arr[nx][ny] > visited[nx][ny]:
                        pass


dx = [0, 1]
dy = [1, 0]
t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    bfs(0, 0)
    for i in range(N):
        print(visited[i])
    print(f'#{tc} {visited[N-1][N-1]}')

