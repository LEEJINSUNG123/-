import sys; sys.stdin = open('최소이동거리.txt')

def dijkstra(s):
    D[s] = 0
    for i in range(N):
        min_v = 11
        for v in range(N+1):
            if not visited[v] and D[v] < min_v:
                min_v = D[v]
                u = v
        visited[u] = 1
        for v in range(N+1):
            if adjM[u][v] and not visited[v]:
                if D[v] > D[u] + adjM[u][v]:
                    D[v] = D[u] + adjM[u][v]

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    adjM = [[0] * (N+1) for _ in range(N+1)]
    D = [11] * (N+1)
    visited = [0] * (N+1)

    for _ in range(E):
        s, e, w = map(int, input().split())
        adjM[s][e] = w
    print(adjM)
    dijkstra(0)
    print(f'#{tc} {D[N]}')
