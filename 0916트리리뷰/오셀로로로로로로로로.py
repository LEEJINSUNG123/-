import sys; sys.stdin = open('오셀로.txt')

def search(x, y, dol):
    arr[x][y] = dol
    if dol == 1:
        reverse_dol = 2
    else:
        reverse_dol = 1
    change = []
    ni = [-1, 1, 0, 0, -1, -1, 1, 1]
    nj = [0, 0, -1, 1, -1, 1, -1, 1]

    for i in range(8):
        nx = x + ni[i]
        ny = y + nj[i]
        if arr[nx][ny] == reverse_dol:
            change.append(i)

    for j in range(len(change)):
        cnt = 0
        while 1:
            nx = x + ni[j]
            ny = y + nj[j]
            if arr[nx][ny] == dol:

            else:
                cnt += 1


t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    arr[N//2][N//2], arr[N//2-1][N//2-1] = 2,2
    arr[N // 2][N // 2 - 1], arr[N//2 - 1][N//2] = 1,1

    # 흑돌은 1 백돌은 2
    for _ in range(M):
        y, x, dol = map(int, input().split())
        x -= 1
        y -= 1
        search(x, y, dol)

    for i in range(N):
        print(arr[i])
