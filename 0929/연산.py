import sys; sys.stdin = open('연산.txt')

def bfs(n, cnt):
    global ans
    q = []
    q.append((n, cnt))
    visited[n] = 1

    while q:
        n, cnt = q.pop(0)

        if n == M:
            return cnt
        for i in range(4):
            if i == 0 and 1 <= n+1 <= 1000000 and not visited[n+1]:
                q.append((n + 1, cnt+1))
                visited[n + 1] = 1

            elif i == 1 and 1 <= n - 1 <= 1000000 and not visited[n-1]:
                q.append((n - 1, cnt+1))
                visited[n - 1] = 1

            elif i == 2 and 1 <= n * 2 <= 1000000 and not visited[n*2]:
                q.append((n * 2, cnt+1))
                visited[n * 2] = 1

            elif i == 3 and 1 <= n - 10 <= 1000000 and not visited[n-10]:
                q.append((n - 10, cnt+1))
                visited[n - 10] = 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    ans = 1000001
    print(f'#{tc} {bfs(N, 0)}')