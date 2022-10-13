import sys; sys.stdin = open('미로2.txt')

di = [-1, 1, 0, 0]
dj = [0, 0,-1, 1]

def bfs(x,y):
    q = []
    q.append([x, y])

    while q:
        v = q.pop(0)
        for i in range(4):
            ni = v[0] + di[i]
            nj = v[1] + dj[i]
            if arr[ni][nj] == 3:
                return 1
            if 0 <= ni < 100 and 0 <= nj < 100 and not arr[ni][nj]:
                q.append([ni, nj])
                arr[ni][nj] = 1
    return 0

def find_start(arr):
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                return i, j

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(100)]
    visited = [[0] * 100 for _ in range(100)]
    x, y = find_start(arr)
    print(f'#{tc} {bfs(x,y)}')

