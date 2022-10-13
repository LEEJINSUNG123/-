'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def bfs(v):
    q = []
    # enque, 방문체크
    q.append(v)
    visited[v] = 1
    print(q)

    while q:
        v = q.pop(0)    # deque -> 하고픈일하기
        print(v, end=' ')
        # 하고픈 일
        for w in adj_list[v]:   # 인접
            if not visited[w]:  # 방문을 안했으면
                q.append(w)
                visited[w] = visited[v] + 1


V, E = map(int, input().split())
temp = list(map(int, input().split()))
adj_list = [[] for _ in range(V+1)]
visited = [0] * (V+1)
for i in range(E):
    s, e = temp[2*i], temp[2*i +1]
    adj_list[s].append(e)
    adj_list[e].append(s)
print(adj_list)

bfs(1)
print(visited)