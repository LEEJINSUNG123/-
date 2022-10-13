import sys; sys.stdin = open('ex2_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    flag = 0
    for i in range(1, 1 << N):  # 공집합은 제외,
        sum_value = 0
        for j in range(N):
            if i & (1 << j):
                sum_value += arr[j]
        if sum_value == 0:
            flag = 1

        # if sum == 0:
        #     for j in range(N):
        #         if i & (1 << j):
        #             print(arr[j], end=" ")
        #     print()
        #     cnt += 1

    print(f'#{tc} {flag}')
