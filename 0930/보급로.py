import sys; sys.stdin = open('보급로.txt')

def dijkstra(x, y):
    # 출발점 설정
    D[x][y] = 0
    # 정점 만큼 돌기
    for _ in range(N*N):
        # 최소값 구하기
        min_v = INF
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 0 and D[i][j] < min_v:
                    min_v = D[i][j]
                    x, y = i, j

        visited[x][y] = 1
        if x == N - 1 and y == N -1:
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if D[nx][ny] >= D[x][y] + arr[nx][ny]:
                    D[nx][ny] = D[x][y] + arr[nx][ny]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
INF = 987654321
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ex, ey = N-1, N-1
    D = [[INF] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    dijkstra(0, 0)
    print(f'#{tc} {D[ex][ey]}')
