import sys; sys.stdin = open('홈방범_input.txt')

def solve():
    ans = 0
    # (x, y)좌표를 기준으로  k = N+1 -> 1로 감소시킴
    for k in range(N+1, 0, -1):  # N+1부터 시작해야 모두 커버 가능
        for x in range(N):
            for y in range(N):
                cnt = 0
                for hx, hy in home:
                    # (x, y) 좌표에서 집까지 거리 < k
                    if abs(x-hx) + abs(y-hy) < k:
                        cnt += 1
                if M * cnt - cost[k] >= 0 and ans < cnt:
                    ans = cnt
    return ans

# 비용을 계산
cost = [0] * 22
cost[1] = 1
for k in range(2, 22):
    cost[k] = k * k + (k-1) * (k-1)

T = int(input())
for tc in range(1, T+1):
    # 도시의 크기와 하나의 집이 지불할 수 있는 비용
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 집의 좌표 저장
    home = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                home.append((i, j))

    print(f'#{tc} {solve()}')
