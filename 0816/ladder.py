import sys; sys.stdin = open("ladder.txt", "r")

def check(arr,x, y):
    if x < 0 or x >= size: return False
    if y < 0 or y >= size: return False
    if arr[x][y] == 0: return False
    if arr[x][y] == 9: return False
    return True


def ladder(arr, x, y):
    while 1:
        if x == 0:
            return y
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if check(arr, nx, ny):
                x = nx
                y = ny
                arr[x][y] = 9 # 방문표시

def find_start(arr):
    for i in range(size):
        if arr[size-1][i] == 2:
            x = size - 1
            y = i
            return x, y

# 좌 우 상
dx = [0, 0, -1]
dy = [-1, 1, 0]
size = 100

for tc in range(1, 11):
    no = int(input())
    arr = [list(map(int, input().split())) for _ in range(size)]

    # 시작점 찾기
    x, y = find_start(arr)
    print(f'#{tc} {ladder(arr,x,y)}')
