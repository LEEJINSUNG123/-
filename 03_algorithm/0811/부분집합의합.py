import sys; sys.stdin = open('부분집합의합_input.txt')

arr = list(range(1, 13))
SIZE = len(arr)
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    ans = 0
    for i in range(1, 1 << SIZE):
        sum = cnt = 0
        for j in range(SIZE):
            if i & (1 << j):
                sum += arr[j]
                cnt += 1
        if sum == K and cnt == N:
            ans += 1
    print(f'#{tc} {ans}')