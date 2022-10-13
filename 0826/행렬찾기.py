import sys; sys.stdin = open('행렬찾기.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = [] # 결과
    count = 0   # 사각형 수

    for i in range(N):
        for j in range(N):
            cnt_garo = cnt_sero = 1
            if arr[i][j] != 0:
                for x in range(1, N-i):
                    if arr[i+x][j] != 0:
                        cnt_sero += 1
                    else:
                        break
                for y in range(1, N-j):
                    if arr[i][j+y] != 0:
                        cnt_garo += 1
                    else:
                        break
                for a in range(cnt_sero):
                    for b in range(cnt_garo):
                        arr[i+a][j+b] = 0

                result.append([cnt_sero, cnt_garo])
                count += 1

    mul = []    # 곱한 결과
    for k in range(len(result)):
        mul.append(result[k][0] * result[k][1])

    mul = list(set(mul))
    mul.sort()

    real_result = []    # 찐 결과 정렬된거

    cnt = 0
    for m in mul:
        temp = []
        ttemp = []  # 세로값 담을거
        for n in range(len(result)):
            if result[n][0] * result[n][1] == m:
                temp.append(result[n])
        if len(temp) == 1 and n == len(result) - 1:
            real_result.extend(temp)
            temp.pop()
        elif len(temp) > 1 and n == len(result) - 1:
            for q in range(len(temp)):
                ttemp.append(temp[q][0])
            ttemp.sort()    # 2, 6, 12
            for p in range(len(ttemp)):
                real_result.append([ttemp[p], m // ttemp[p]])
        # print(tttemp)
    print(f'#{tc} {count}', end=' ')
    for r in real_result:
        print(*r, end=' ')
    print()





