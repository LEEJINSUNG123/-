import sys; sys.stdin = open('오셀로_input.txt')
def print_arr():
    for i in range(1, N+1):
        for j in range(1, N+1):
            print(arr[i][j], end=' ')
        print()
    print()

def check(sx, sy, dol):
    for i in range(8):
        # sx와 sy를 시작접으로 기억해야함.
        nx = sx + dx[i]
        ny = sy + dy[i]
        flag = False
        # 벽이 아니면 주어진 방향으로 계속 증가
        while 0 < nx <= N and 0 < ny <= N:
            # 0 이면 break
            if arr[nx][ny] == 0: break
            # 같은 돌이면, flag 체크하고 endX, endY변경
            if arr[nx][ny] == dol:
                flag = True
                ex = nx
                ey = ny
                break   # 가까운 위치의 같은 색상의 돌을 찾고 그만
            nx += dx[i]
            ny += dy[i]
        # 같은 색상의 돌이 있으면, (sx, sy) -> (ex, ey)까지의 돌의 색상 변경
        if flag:
            nx = sx
            ny = sy
            while not(nx == ex and ny == ey):
                nx += dx[i]
                ny += dy[i]
                arr[nx][ny] = dol


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]

    # 초기화
    mid = N // 2
    arr[mid][mid] = arr[mid+1][mid+1] = 2
    arr[mid][mid+1] = arr[mid+1][mid] = 1
    # print_arr()

    # 돌놓기
    for i in range(M):
        x, y, dol = map(int, input().split())
        arr[x][y] = dol
        check(x, y, dol)
        # print_arr()

    # 돌세기
    B = 0
    W = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 1: B += 1
            if arr[i][j] == 2: W += 1
    print(f'#{tc} {B} {W}')