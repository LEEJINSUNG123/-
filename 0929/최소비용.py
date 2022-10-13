import sys; sys.stdin = open('최소비용.txt')

def bfs(x, y):
    global cnt
    q = []
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                


def dijkstra(s):
    # 출발점 선택
    D[s] = 0
    # for 모든 도시가 선택될 때 까지
    for i in range(V):
        # 최소값찾기
        min_v = 987654321
        for v in range(V):
            if not visited[v] and D[v] < min_v:
                min_v = D[v]
                u = v    # 선택한 도시
        # 방문체크
        visited[u] = 1
        # 업데이트 : u에 인접한 정점, 방문 안한 정점 ->  가중치
        for v in range(V):
            if adj[u][v] and not visited[v]:
                if D[v] > D[u] + adj[u][v]:  # 핵심
                    D[v] = D[u] + adj[u][v]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    adjM = [[0] * N for _ in range(N)]
    D = [[1000] * N] # 가중치
    w = [i for i in range(V)]
    print(w)

    bfs(0, 0)
    for i in range(N):
        print(adjM[i])