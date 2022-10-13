import sys; sys.stdin = open('노드의거리.txt')

def bfs(s,g):
    global flag
    visited[s] = 1
    q = []
    q.append(s)

    while q:
        qq = q.pop()
        for w in adj_list[qq]:
            if not visited[w]:
                visited[w] = visited[qq] + 1
                q.append(w)
                if w == g:
                    flag = 1
                    return visited[w]

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    for i in range(E):
        s, e = map(int, input().split())
        adj_list[s].append(e)
        adj_list[e].append(s)
    S, G = map(int, input().split())
    flag = 0
    x = bfs(S, G) - 1
    if flag:
        print(f'#{tc} {x}')
    else:
        print(f'#{tc} 0')
