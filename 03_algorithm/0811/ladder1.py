import sys; sys.stdin = open('ladder1_input.txt')
sys.stdout = open('ladder1_output.txt', 'w')

def find_start(arr):
    for i in range(SIZE):
        if arr[SIZE-1][i] == 2:
            x = SIZE - 1
            y = i
            return x, y


def ladder(arr, x, y):
    while True:
        if x == 0:
            return y
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < SIZE and 0 <= ny < SIZE and arr[nx][ny] == 1:
                x = nx
                y = ny
                arr[x][y] = 9 # 방문표시


# 좌우를 먼저해야 함
dx = [0, 0, -1]
dy = [-1, 1, 0]
T = 10
SIZE = 100
for tc in range(1, T+1):
    no = int(input())
    arr = [list(map(int, input().split())) for _ in range(SIZE)]

    # 시작점 찾기
    x, y = find_start(arr)
    print(f'#{tc} {ladder(arr, x, y)}')

    for a in arr:
        print(*a)