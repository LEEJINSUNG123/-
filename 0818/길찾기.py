# dfs

import sys; sys.stdin = open("길찾기.txt")

def dfs(v):
    # 방문처리
    visited[v] = 1
    global flag
    if v == B:
        flag = 1
    for w in adj_list[v]:
        # 방문 안한 정점 있으면
        if visited[w] == 0:
            dfs(w)
    return

for tc in range(1, 11):
    V = 100
    T, E = map(int, input().split())
    adj_list = [[] for _ in range(V)]
    visited = [0] * V
    temp = list(map(int, input().split()))
    A, B = 0, 99
    for i in range(E):
        s, e = temp[2*i], temp[2*i+1]
        # 단방향
        adj_list[s].append(e)
    flag = 0
    dfs(A)
    print(f'#{tc} {flag}')