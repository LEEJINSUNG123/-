import sys; sys.stdin = open('색칠하기_input.txt')
def print_arr(arr):
    for item in arr:
        print(*item)


T = int(input())
SIZE = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * SIZE for _ in range(SIZE)]

    # 색칠하기
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                arr[i][j] += color   # 누적

    # print_arr(arr)
    # print()
    # 겹쳐진 칸수 카운팅
    cnt = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if arr[i][j] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')

