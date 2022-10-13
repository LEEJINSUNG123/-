import sys; sys.stdin = open('오목판정.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    # print(arr)
    flag = 0

    # 가로
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 'o':
                cnt += 1
            else:
                cnt = 0
            if cnt == 5:
                flag = 1
                break
        if cnt == 5:
            break
    # 세로
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 'o':
                cnt += 1
            else:
                cnt = 0
            if cnt == 5:
                flag = 1
                break
        if cnt == 5:
            break
    # 대각선
    cnt1 = cnt2 = 0
    for i in range(N):
        if arr[i][i] == 'o':
            cnt1 += 1
        else:
            cnt1 = 0
        if arr[i][N-i-1] == 'o':
            cnt2 += 1
        else:
            cnt2 = 0
        if cnt1 == 5 or cnt2 == 5:
            flag = 1
            break

    # 미니 대각선
    cnt1 = cnt2 = 0
    for i in range(1, N-5+1):
        for j in range(N-i):
            if arr[j][j+i] == 'o':
                cnt1 += 1
            else:
                cnt1 = 0
            if arr[j][N - j - 1 - i] == 'o':
                cnt2 += 1
            else:
                cnt2 = 0
            if cnt1 == 5 or cnt2 == 5:
                flag = 1
                break

        # 미니 대각선
        cnt1 = cnt2 = 0
        for i in range(1, N - 5 + 1):
            for j in range(N - i):
                if arr[j+i][j] == 'o':
                    cnt1 += 1
                else:
                    cnt1 = 0
                if arr[j+i][N - j - 1] == 'o':
                    cnt2 += 1
                else:
                    cnt2 = 0
                if cnt1 == 5 or cnt2 == 5:
                    flag = 1
                    break

    if flag:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')