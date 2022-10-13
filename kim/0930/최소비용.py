import sys; sys.stdin= open('최소비용.txt')
import heapq

def dijkstra(x, y):
    # heap = []
    D[x][y] = 0
    # heapq.heappush(heap, (D[x][y], x, y))   # 가중치, x, y 가중치로 정렬함

    # while heap:
    for _ in range(N*N):
        # 최소값 구하기
        min_v = INF
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 0 and D[i][j] < min_v:
                    min_v = D[i][j]
                    x, y = i,j
        # d, x, y = heapq.heappop(heap)

        # 방문처리
        visited[x][y] = 1
        if x == N - 1 and y == N-1:
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                diff = 0
                if arr[nx][ny] > arr[x][y]:
                    diff = arr[nx][ny] - arr[x][y]
                if D[nx][ny] > D[x][y] + 1 + diff:
                    D[nx][ny] = D[x][y] + 1 + diff
                    # heapq.heappush(heap, (D[nx][ny], nx, ny))


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
INF = 987654321
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    D = [[INF] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    dijkstra(0, 0)
    print(f'#{tc} {D[N-1][N-1]}')