import sys; sys.stdin = open('피자화덕.txt')

T = int(input())
for  tc in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int,input().split()))
    CC = [0] * (M+1)
    for idx, value in enumerate(C):
        CC[idx+1] = [idx+1, value]
    # print(CC)

    Q = []
    for _ in range(N):
        Q.append(CC.pop(0))
    print(CC)
    print(Q)
    idx = M
    while len(Q) > 1:
        t = Q.pop(0)
        t[1] = t[1] // 2
        if t[1] > 0:
            Q.append(t)
        elif idx <= M:
            Q.append(t)
            idx += 1