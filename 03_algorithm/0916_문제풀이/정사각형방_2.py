import time

start = time.time()

import sys

sys.stdin = open("정사각형방_input.txt")

from collections import deque


def bfs(x, y):
    deq = deque()
    sol = []
    deq.append((x, y))
    visit[x][y] = 1
    sol.append(arr[x][y])
    while deq:
        x, y = deq.popleft()
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0 and \
                    abs(arr[nx][ny] - arr[x][y]) == 1:
                deq.append((nx, ny))
                visit[nx][ny] = 1
                sol.append(arr[nx][ny])
    return min(sol), len(sol)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    num = N * N
    cnt = 0

    for x in range(N):
        for y in range(N):
            if visit[x][y] == 0:
                temp_num, temp_cnt = bfs(x, y)
                if cnt < temp_cnt or cnt == temp_cnt and num > temp_num:
                    cnt = temp_cnt
                    num = temp_num
    print("#{} {} {}".format(tc, num, cnt))

print(time.time() - start)
