import sys; sys.stdin = open('스도쿠_input.txt')
def sudoku(arr):
    # 행검사
    for i in range(9):
        count = [0] * 10
        for j in range(9):
            count[arr[i][j]] += 1
            if count[arr[i][j]] > 1:
                return 0

    # 열검사
    for i in range(9):
        count = [0] * 10
        for j in range(9):
            count[arr[j][i]] += 1
            if count[arr[j][i]] > 1:
                return 0

    # 3X3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            count = [0] * 10
            for x in range(3):
                for y in range(3):
                    count[arr[i+x][j+y]] += 1
                    if count[arr[i+x][j+y]] > 1:
                        return 0

    return 1

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{tc} {sudoku(arr)}')
