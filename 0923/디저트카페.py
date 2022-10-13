import sys; sys.stdin = open('디저트카페.txt')



dx = [1, 1, -1, -1]
dy = [-1, 1, 1, -1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 투어를 성공한 카페
    ans = 0
    # 시작하는 곳
    for i in range(N-2):
        for j in range(1, N-1):
            sx, sy = i, j
            tour = [arr[sx][sy]]
            nx, ny = sx, sy
            for k in range(4):
                for l in range((N-2)**2):
                    nx += dx[k]
                    ny += dy[k]
                    if nx == sx and ny == sy:
                        ans += 1
                    if 0 <= nx < N and 0 <= ny < N:
                        # 메뉴 중첩되면
                        if arr[nx][ny] in tour:
                            break
                        # 처음 먹으면
                        else:
                            tour.append(arr[nx][ny])
                    else:
                        break
    if ans:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} {ans}')