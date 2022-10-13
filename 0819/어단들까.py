import sys; sys.stdin = open("어단들까.txt")

t = int(input())
for tc in range(1, t+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr2 = [[0] * N for _ in range(N)]
    total = 0

    for i in range(N):
        for j in range(N):
            if j > i:
                arr2[i][j], arr2[j][i] = arr[j][i], arr[i][j]
            elif i == j:
                arr2[i][j] = arr[i][j]

    for i in range(N):
        cnt = 0
        arr[i].append(0)
        for j in range(N+1):
            if arr[i][j] == 1:
                cnt += 1
            elif arr[i][j] == 0:
                if cnt == K:
                    total += 1
                    cnt = 0
                else:
                    cnt = 0

    for i in range(N):
        cnt = 0
        arr2[i].append(0)
        for j in range(N+1):
            if arr2[i][j] == 1:
                cnt += 1
            elif arr2[i][j] == 0:
                if cnt == K:
                    total += 1
                    cnt = 0
                else:
                    cnt = 0

    print(f'#{tc} {total}')