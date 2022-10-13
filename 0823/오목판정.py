import sys; sys.stdin = open('오목판정.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(str, input())) for _ in range(n)]
    # print(arr)
    flag = 0
    # 가로
    for i in range(n):
        cnt = 0
        arr[i].append('.')
        for j in range(n+1):
            if arr[i][j] == 'o':
                cnt += 1
            else:
                if cnt >= 5:
                    flag = 1
                cnt = 0
        # print(arr)
        arr[i].pop()
    # print(arr)

    # 세로
    arr.append(['.']*n)
    for i in range(n):
        cnt = 0
        for j in range(n+1):
            if arr[j][i] == 'o':
                cnt += 1
            else:
                if cnt >= 5:
                    flag = 1
                cnt = 0
    arr.pop()

    # 대각선
    cnt = 0
    for i in range(n):
        if arr[i][i] == 'o':
            cnt += 1
        else:
            if cnt >= 5:
                flag = 1
            cnt = 0
    if cnt >= 5:
        flag = 1
    cnt = 0



    for i in range(n):
        if arr[i][n-1-i] == 'o':
            cnt += 1
        else:
            if cnt >= 5:
                flag = 1
            cnt = 0
    if cnt >= 5:
        flag = 1
    cnt = 0

    x = n
    r = n
    # 우측 아래 위로
    for i in range(n - 5):
        x -= 1
        y = 0
        ni = x - 1
        nj = y
        r -= 1
        for j in range(r):
            if arr[j][r - 1 - j] == 'o':
                cnt += 1
            else:
                if cnt >= 5:
                    flag = 1
                cnt = 0
        if cnt >= 5:
            flag = 1
        cnt = 0

    y = 0
    r = n
    # 우측 아래 오른쪽
    for i in range(n - 5):
        x = n - 1
        y += 1
        ni = x
        nj = y
        for j in range(r):
            if arr[j][r - 1 - j] == 'o':
                cnt += 1
            else:
                if cnt >= 5:
                    flag = 1
                cnt = 0
        if cnt >= 5:
            flag = 1
        cnt = 0

    if flag:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')