import sys; sys.stdin = open("스도쿠.txt")

t = int(input())

for tc in range(1, t+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result_garo = result_sero = result_nemo = 0

    # 가로 검증
    for i in range(9):
        cnt = 0
        count = [0] * 9
        for j in range(9):
            count[arr[i][j]-1] = 1
        for c in count:
            if c != 0:
                cnt += 1
        if cnt == 9:
            result_garo += 1

    # 세로 검증
    for i in range(9):
        cnt = 0
        count = [0] * 9
        for j in range(9):
            count[arr[j][i]-1] = 1
        for c in count:
            if c != 0:
                cnt += 1
        if cnt == 9:
            result_sero += 1

    # 미니 네모 검증
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            cnt = 0
            count = [0] * 9
            for x in range(3):
                for y in range(3):
                    count[arr[i+x][j+y]-1] = 1
            for c in count:
                if c != 0:
                    cnt += 1
            if cnt == 9:
                result_nemo += 1

    if result_garo == 9 and result_sero == 9 and result_nemo == 9:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')