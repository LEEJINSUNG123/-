import sys; sys.stdin = open("통나무자르기.txt")

t = int(input())

for tc in range(1, t+1):
    N = int(input())
    if tc % 2:
        flag = 1
    else:
        flag = -1
    while N >= 2:
        N = float(N / 2)
        flag = -flag
    if flag == 1:
        print(f'#{tc} Bob')
    else:
        print(f'#{tc} Alice')
