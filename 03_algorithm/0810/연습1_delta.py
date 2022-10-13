import sys
sys.stdin = open('연습1_delta.txt')


def cal_abs(x, y):
    if x - y > 0:
        return x - y
    else:
        return y - x


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    total = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                # 벽체크
                if 0 <= ni < N and 0 <= nj < N:
                    total += cal_abs(arr[i][j], arr[ni][nj])
    print(f'#{tc} {total}')

