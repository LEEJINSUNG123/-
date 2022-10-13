import sys; sys.stdin = open("색칠하기.txt")

def print_arr(arr):
    for item in arr:
        print(*item)

t = int(input())
for tc in range(1, t+1):

    N = int(input())
    arr = [[0] * 10 for _ in range(10)]

    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                arr[i][j] += color

    # print_arr(arr)
    # print()
    total = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                total += 1
    print(f'#{tc} {total}')




'''
t = int(input())

for tc in range(1, t+1):
    n = int(input())
    board = [[0] * 10 for _ in range(10)]
    total = 0
    for a in range(n):
        x1, y1, x2, y2, color = map(int, input().split())
        # 색칠칸 값 넣어주기
        if color == 1:
            for i in range(x2-x1+1):
                for j in range(y2-y1+1):
                    board[x1+i][y1+j] += 1
        elif color == 2:
            for i in range(x2-x1+1):
                for j in range(y2-y1+1):
                    board[x1+i][y1+j] += 2
    # 겹치는 값 3 찾기
    for i in range(10):
        for j in range(10):
            if board[i][j] == 3:
                total += 1
    print(f'#{tc} {total}')
'''
# 플러드필 = dfs탐색