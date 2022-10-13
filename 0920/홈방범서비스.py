import sys; sys.stdin = open('홈방범서비스.txt')

def solve()
    ans = 0
    # (x, y)

# 비용을 계산
cost = [0] * 22
cost[1] = 1
for k in range(2,22):
    cost[k] = k * k + (k-1) * (k-1)

t = int(input())
for tc in range(1, 1+t):
    # 도시의 크기와 집을 할 스 있는 내용
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    home = []
    for i in range(N):
        for j in range(N):
