import sys; sys.stdin = open("배열최소합.txt")

def perm(n, k, ssum):
    global min_v
    if min_v < ssum: return
    if n == k:
        # sum_v = 0
        # for i in range(N):
        #     sum_v += arr[i][A[i]]
        # if min_v > sum_v:
        #     min_v = sum_v
        if min_v > ssum:
            min_v = ssum
    else:
        for i in range(k, n):
            A[k], A[i] = A[i], A[k]
            perm(n, k+1, ssum + arr[k][A[k]])
            A[k], A[i] = A[i], A[k]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 987654321
    A = list(range(N))
    perm(N, 0, 0)
    print(f'#{tc} {min_v}')