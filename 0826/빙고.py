import sys; sys.stdin = open('빙고.txt')


def bingo():
    check_diag1 = 0
    check_diag2 = 0
    total = 0
    for i in range(5):
        for j in range(5):
            # 번 호 부 르 기
            x = num_in[i][j]
            for a in range(5):
                for b in range(5):
                    # 번 호 체 크
                    if arr[a][b] == x:
                        arr[a][b] = 'x'
                    print(arr)

                    # 빙 고 검 사
                    for p in range(5):
                        cnt = 0
                        if len(check_sero) > 0:
                            for ww in range(len(check_sero)):
                                if check_sero[ww] == p:
                                    continue
                                else:
                                    for q in range(5):
                                        if arr[p][q] == 'x':
                                            cnt += 1
                        else:
                            for q in range(5):
                                if arr[p][q] == 'x':
                                    cnt += 1
                        if cnt == 5:
                            check_sero.append(p)
                            total += 1

                    for p in range(5):
                        cnt = 0
                        if len(check_garo) >0:
                            for ww in range(len(check_garo)):
                                if check_garo[ww] == p:
                                    continue
                                else:
                                    for q in range(5):
                                        if arr[q][p] == 'x':
                                            cnt += 1
                        else:
                            for q in range(5):
                                if arr[q][p] == 'x':
                                    cnt += 1
                        if cnt == 5:
                            check_garo.append(p)
                            total += 1

                    cnt1 = 0
                    if check_diag1 == 0:
                        for w in range(5):
                            if arr[w][w] == 'x':
                                cnt1 += 1
                        if cnt1 == 5:
                            check_diag1 = 1
                            total += 1
                    else:
                        pass

                    cnt2 = 0
                    if check_diag2 == 0:
                        for w in range(5):
                            if arr[w][5 - 1 - w] == 'x':
                                cnt2 += 1
                        if cnt2 == 5:
                            check_diag2 = 1
                            total += 1
                    else:
                        pass

                    if total == 3:
                        return i, j
    return 0, 0

arr = [list(map(int, input().split())) for _ in range(5)]
num_in = [list(map(int, input().split())) for _ in range(5)]
check_garo = []
check_sero = []

# print(arr)
x, y = bingo()
print(5*x + (y+1))