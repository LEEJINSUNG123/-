# dfs
import sys; sys.stdin = open("그래프경로.txt")

def dfs(v):
    # 방문처리
    visited[v] = 1
    global flag
    if v == end:
        flag = 1
    for w in adj_list[v]:
        # 방문 안한 정점 있으면
        if visited[w] == 0:
            dfs(w)
    return

t = int(input())
for tc in range(1, t+1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    temp = []
    for _ in range(E):
        ve = list(map(int, input().split()))
        temp.extend(ve)
    start, end = map(int, input().split())
    for i in range(E):
        s, e = temp[2*i], temp[2*i+1]
        # 단방향
        adj_list[s].append(e)
    flag = 0
    dfs(start)
    print(f'#{tc} {flag}')