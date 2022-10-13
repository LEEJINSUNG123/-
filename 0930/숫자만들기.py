import sys; sys.stdin = open('숫자만들기.txt')

def dfs(n, k, ssum):
    global max_v
    global min_v
    if len(oper) == k:
        return
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                dfs(n+1, k+1, ssum )
                visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    temp = list(map(int, input().split()))
    num = list(map(int, input().split()))
    oper = []
    for i in range(4):
        for j in range(temp[i]):
            if i == 0:
                oper.append('+')
            elif i == 1:
                oper.append('-')
            elif i == 2:
                oper.append('*')
            elif i == 3:
                oper.append('/')
    min_v = 987654321
    max_v = 0
    visited = [0] * N
    print(oper)
    dfs(0, 0, num[0])
