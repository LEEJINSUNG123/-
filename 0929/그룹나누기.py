import sys; sys.stdin = open('그룹나누기.txt')

def dfs(n):
    visited[n] = 1
    for i in adj_list[n]:
        if not visited[i]:
            dfs(i)

def bfs(n):
    pass

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [0] * (N+1)
    adj_list = [[] for _ in range(N+1)]

    for i in range(M):
        s, e = arr[2*i], arr[2*i + 1]
        adj_list[s].append(e)
        adj_list[e].append(s)

    arr = set(arr)
    cnt = 0
    for i in arr:
        if visited[i] == 0:
            dfs(i)
            cnt += 1
        else:
            pass
    print(f'#{tc} {cnt + (visited.count(0)-1)}')


