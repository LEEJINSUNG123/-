import sys; sys.stdin = open("부분집합의합.txt")

t = int(input())
arr = [i for i in range(1, 13)]
SIZE = len(arr)

for tc in range(1, t+1):
    N, K = map(int, input().split())
    ans = 0

    for i in range(1, 1<<SIZE):
        sum = cnt = 0
        for j in range(SIZE):
            if i & (1<<j):
                sum += arr[j]
                cnt += 1
        if sum == K and cnt == N:
            ans += 1
    print(f'#{tc} {ans}')




'''
t = int(input())

for tc in range(1, t+1):
    a = [i for i in range(1, 13)]
    n, k = map(int, input().split())
    count = 0

    for i in range(1 << 12):
        cnt = total = 0
        for j in range(12):
            if i & (1 << j):
                cnt += 1
                total += a[j]
        if cnt == n:
            if total == k:
                count += 1

    print(f'#{tc} {count}')
'''