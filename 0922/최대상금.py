import sys; sys.stdin = open('최대상금.txt')

def comb(n, r):
    global max_v
    l = len(n)
    if r == K:
        d = int(''.join(n))
        if d > max_v:
            max_v = d
        return
    if ''.join(n) in memo[r]:
        return
    memo[r].append(''.join(n))
    for i in range(l-1):
        for j in range(i+1, l):
            n[i], n[j] = n[j], n[i]
            print(memo)
            comb(n, r+1)
            n[i], n[j] = n[j], n[i]

t = int(input())
for tc in range(1, t+1):
    N, K = map(str, input().split())
    memo = [[] for _ in range(int(K))]
    n = list(N)
    max_v = 0
    comb(n, 0)

