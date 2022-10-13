import sys; sys.stdin = open("그래프경로.txt")

def dfs(v):
    global flag
    visited[v] = 1
    print(v, end=' ')
    if v == G:
        # flag = 1
        return 1

    for w in adj_list[v]:
        if visited[w] == 0:
            if dfs(w) == 1:
                return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for _ in range(E):
        a, b = map(int, input().split())
        adj_list[a].append(b)
    print(adj_list)
    S, G = map(int, input().split())
    flag = 0
    dfs(S)
    print(f'#{tc} {visited[G]}')