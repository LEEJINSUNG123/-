import sys
sys.stdin = open('view_input.txt', 'r')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0

    for i in range(2, N-2):
        # i-2, i-1, i+1, i+2
        max_value = 0
        for j in range(5):
            if j != 2:
                if max_value < arr[i-2+j]:
                    max_value = arr[i-2+j]
        # 좌우 2개의 최대값이 i값보다 작은경우 조망권 확보
        if arr[i] > max_value:
            ans += arr[i] - max_value

    print(f'#{tc} {ans}')
