import sys; sys.stdin = open("magnetic.txt")

for tc in range(1, 11):
    size = int(input())
    arr = [list(map(int, input().split())) for _ in range(size)]
    cnt = 0

    while 1:
        for i in range(100):
            # num = 0
            for j in range(100):
                # if arr[j][i] == 1:
                #     num = 1
                if arr[j][i] == 2 and arr[j-1][i] == 0:
                    arr[j][i], arr[j-1][i] = 0, 2
                elif arr[j][i] == 2 and arr[j-1][i] == 2:
                    arr[j-2][i], arr[j-1][i] = 2, 2
                elif arr[j][i] == 2 and arr[j-1][i] == 1:
                    arr[j][i], arr[j-1][i] = 0, 0
                    cnt += 1
                    # num = 0
        print(cnt)
    print(f'#{tc} {cnt}')