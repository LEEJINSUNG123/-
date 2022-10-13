import sys; sys.stdin = open('최소신장트리.txt')

def prim(n, V):
    MST = [0] * (V+1)
    key = [10] * (V+1)
    key[n] = 0
    for _ in range(V):
        u = 0
        min_v = 10
        for i in range(V+1):
            if MST[i] == 0 and key[i] < min_v:
                u = i
                min_v = key[i]
        MST[u] = 1
        for v in range(V+1):
            if MST[v] == 0 and adjM[u][v] > 0:
                key[v] = min(key[v], adjM[u][v])
    return sum(key)

def prim2(n, V):
    MST = [0] * (V+1)
    MST[n] = 1
    s = 0
    for _ in range(V):
        u = 0
        min_v = 10
        for i in range(V+1):
            if MST[i] == 1:
                for j in range(V+1):
                    if adjM[i][j] > 0 and MST[j] == 0 and min_v > adjM[i][j]:
                        u = j
                        min_v = adjM[i][j]
        s += min_v
        MST[u] = 1
    return s

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjM = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        n1, n2, w = map(int, input().split())
        adjM[n1][n2] = w
        adjM[n2][n1] = w
    print(f'#{tc} {prim2(0, V)}')
