import sys; sys.stdin = open('최소이동거리.txt')

def dijkstra(s):
    # 출발점 설정
    D[s] = 0
    # 0 ~ N 번 반복
    for i in range(N+1):
        # 최소값 찾기
        minV = INF
        for v in range(N+1):
            if not visited[v] and D[v] < minV:
                minV = D[v]
                u = v
        # 방문처리
        visited[u] = 1
        if u == N:
            return D[u]
        # 방문안한 인접 정점 갱신
        for v in range(N+1):
            if adj[u][v] and not visited[v]:
                if D[v] > D[u] + adj[u][v]:
                    D[v] = D[u] + adj[u][v]


INF = 987654321
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    adj = [[0] * (N+1) for _ in range(N+1)]
    D = [INF] * (N+1)
    visited = [0] * (N+1)

    for i in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w

    print(f'#{tc} {dijkstra(0)}')


    def dfs(s, k, d):
        global ans
        visited[s] = 1
        # print(s, end=' ')
        if N - 1 == k:
            if ans > d:
                ans = d
            return
        else:
            for e in adj_list[s]:
                if not visited[e]:
                    visited[e] = 1
                    temp = adjM[s][e] * E
                    dfs(e, k + 1, d + temp)
                    visited[e] = 0
