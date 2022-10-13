import sys; sys.stdin = open("기지국.txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input()) # 50 이하
    arr = [list(map(str, input())) for _ in range(n)]
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'A':    # 1칸 커버
                for x in range(4):
                    ni = i + di[x]
                    nj = j + dj[x]
                    if ni >= 0 and ni < n and nj >= 0 and nj < n:
                        arr[ni][nj] = 'X'
            elif arr[i][j] == 'B':  # 2칸 커버
                for x in range(8):
                    if x < 4:
                        ni = i + di[x]
                        nj = j + dj[x]
                        if ni >= 0 and ni < n and nj >= 0 and nj < n:
                            arr[ni][nj] = 'X'
                    else:
                        ni = i + 2*di[x]
                        nj = j + 2*dj[x]
                        if ni >= 0 and ni < n and nj >= 0 and nj < n:
                            arr[ni][nj] = 'X'
            elif arr[i][j] == 'C':  # 3칸 커버
                for x in range(12):
                    if x < 4:
                        ni = i + di[x]
                        nj = j + dj[x]
                        if ni >= 0 and ni < n and nj >= 0 and nj < n:
                            arr[ni][nj] = 'X'
                    elif x < 8:
                        ni = i + 2 * di[x]
                        nj = j + 2 * dj[x]
                        if ni >= 0 and ni < n and nj >= 0 and nj < n:
                            arr[ni][nj] = 'X'
                    else:
                        ni = i + 3 * di[x]
                        nj = j + 3 * dj[x]
                        if ni >= 0 and ni < n and nj >= 0 and nj < n:
                            arr[ni][nj] = 'X'
    total = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'H':
                total += 1
    print(f'#{tc} {total}')