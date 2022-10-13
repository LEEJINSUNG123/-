from copy import deepcopy

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
temp = deepcopy(arr)

for i in range(N):
    for j in range(M):
        # 벽을 세울 수 있는 곳
        if temp[i][j] == 0:


