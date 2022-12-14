def bfs(x, y):
    q = []
    q.append((x, y))  # 리스트로 큐 구현, 좌표는 튜플로 저장
    visited[x][y] = 1  # 방문 표시
    while len(q) != 0:
        x, y = q.pop(0)  # deQ
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ny < 0 or ny == N: continue      # 인덱스 체크를 먼저 해야
            if nx < 0 or nx == N: continue
            if maze[nx][ny] == 3:               # 출구인 경우
                return 1
            elif maze[nx][ny] == 0 and visited[nx][ny] == 0:  # 갈수 있는 곳 저장
                q.append([nx, ny])  # enQ
                visited[nx][ny] = 1
    return 0  # 출구에 가지 못하고 모든 칸 방문


def findStart(data):
    for y in range(N):
        for x in range(N):
            if data[y][x] == 2:
                return y, x


T = 10
N = 100
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for tc in range(T):
    no = int(input())
    maze = [list(map(int, input())) for i in range(N)]  # 미로를 중첩리스트로 저장
    visited = [[0 for _ in range(N)] for _ in range(N)]
    sy, sx = findStart(maze)
    print('#{} {}'.format(tc + 1, bfs(sx, sy)))