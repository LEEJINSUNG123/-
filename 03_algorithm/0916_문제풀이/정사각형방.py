import time
start = time.time()

import sys; sys.stdin = open('정사각형방_input.txt')
from collections import deque

def bfs(x, y):
    max_value = 0
    deq = deque()
    deq.append((x, y))
    visited[x][y] = 1
    while deq:
        x, y = deq.popleft()
        if max_value < visited[x][y]:
            max_value = visited[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and \
                arr[x][y] + 1 == arr[nx][ny]:
                deq.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    return max_value


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    ans = 987654321
    cnt = 0
    for x in range(N):
        for y in range(N):
            ret = bfs(x, y)
            if cnt < ret:
                cnt = ret
                ans = arr[x][y]
            elif ret == cnt and ans > arr[x][y]:
                ans = arr[x][y]
    print(f'#{tc} {ans} {cnt}')

print(time.time() - start)