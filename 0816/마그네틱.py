import sys; sys.stdin = open("마그네틱.txt","r")

for tc in range(1, 11):
    n = int(input()) # 100
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0

    while 1:
        cntt = 0
        for i in range(n):
            for j in range(n):
                if arr[i][j] == 1:
                    if i == 0:
                        arr[i][j] = 0
                    else:
                        arr[i][j] -= 1
                        # if arr[i - 1][j] == 0 or arr[i - 1][j] == 2:
                        arr[i - 1][j] += 1
                        # else:
                        #     pass

        for i in range(n):
            for j in range(n):
                if arr[i][j] == 3:
                    arr[i][j] = 0
                    cnt += 1

        for i in range(n):
            for j in range(n):
                if arr[i][j] == 2:
                    if i == 99:
                        arr[i][j] = 0
                    else:
                        arr[i][j] -= 2
                        if arr[i + 1][j] == 0 or arr[i + 1][j] == 1:
                            arr[i + 1][j] += 2
                        else:
                            pass

        for i in range(n):
            for j in range(n):
                if arr[i][j] == 3:
                    arr[i][j] = 0
                    cnt += 1
        print(f'#{tc} {cnt}')
        # for i in range(n):
        #     for j in range(n):
        #         if arr[i][j] == 0:
        #             cntt += 1
        #
        # if cntt == 100:
        #     break
    print(f'#{tc} {cnt}')