import sys; sys.stdin = open('연산.txt')
from collections import deque

def bfs(n):
    visited[n] = 1
    q = [n]
    q = deque(q)

    while q:
        n = q.popleft()
        if n == M:
            return visited[n] - 1
        for t in [n+1, n-1, n*2, n-10]:
            if 0 < t <= 1000000 and not visited[t]:
                q.append(t)
                visited[t] = visited[n] + 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    print(f'#{tc} {bfs(N)}')
