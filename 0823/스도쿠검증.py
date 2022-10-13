import sys; sys.stdin = open("스도쿠검증.txt")

# sum 45로 하면 안됨.
# 카운팅정렬.

t = int(input())
for tc in range(1, t+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    flag = 1

    for i in range(9):
        count = [0] * 10
        for j in range(9):
            count[arr[i][j]] += 1
            if count[arr[i][j]] > 1:
                flag = 0

    for i in range(9):
        count = [0] * 10
        for j in range(9):
            count[arr[j][i]] += 1
            if count[arr[j][i]] > 1:
                flag = 0

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            count = [0] * 10
            for x in range(3):
                for y in range(3):
                    count[arr[i+x][j+y]] += 1
                    if count[arr[i+x][j+y]] > 1:
                        flag = 0

    print(f'#{tc} {flag}')