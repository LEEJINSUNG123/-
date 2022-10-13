import sys; sys.stdin = open('요리사.txt')

def comb(n, r, k, s):
    if k == r:
        print(t)
    else:
        for i in range(s, n - r + 1 + k):
            t[k] = a[i]
            comb(n, r, k+1, i+1)

# N = 4
# R = 3
# a = [1, 2, 3, 4]
# t = [0] * R
# comb(N, R, 0, 0)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    r = N // 2
    a = [i for i in range(N)]
    t = [0] * r
    comb(N, r, 0, 0)