import sys; sys.stdin = open('하나로.txt')

def dfs(s, k, d):
    global ans
    visited[s] = 1
    # print(s, end=' ')
    if N-1 == k:
        if ans > d:
            ans = d
        return
    else:
        for e in adj_list[s]:
            if not visited[e]:
                visited[e] = 1
                temp = adjM[s][e] * E
                dfs(e, k+1, d + temp)
                visited[e] = 0

def dijkstra(s):
    # 출발점 설정
    D[s] = 0
    # 정점만큼 돌기
    for i in range(N):
        # 최소값 찾기
        min_v = INF
        for v in range(N):
            if not visited[v] and D[v] < min_v:
                min_v = D[v]
                u = v

        # 방문처리
        visited[u] = 1

        # 인접한 정점 업데이트
        for v in range(N):
            if adjM[u][v] and not visited[v]:
                if D[v] > D[u] + adjM[u][v]:
                    D[v] = D[u] + adjM[u][v]

INF = 98765432100
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())
    adjM = [[0] * N for _ in range(N)]
    adj_list = [[] * N for _ in range(N)]
    D = [INF] * N
    visited = [0] * N

    for i in range(N):
        for j in range(N):
            if i != j:
                adj_list[i].append(j)

    ans = 0
    for i in range(N):
        for j in range(N):
            if i != j:
                # L 제곱
                d = ((x[i] - x[j])**2 + (y[i] - y[j])**2) * E
                adjM[i][j] = adjM[j][i] = d

    dijkstra(0)
    print(D)
    print(f'#{tc} {D[N-1]}')