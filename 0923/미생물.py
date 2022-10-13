import sys; sys.stdin = open('미생물.txt')

def print_arr():
    for i in range(N):
        print(arr[i])
    print()

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}')
    N, M, K = map(int, input().split())
    arr = [[0,1] * N for _ in range(N)]
    for i in range(K):
        x, y, n, d = map(int, input().split())
        arr[x][y] = [n,d]

    # 상 하 좌 우
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    print_arr()

    for i in range(1, N-1):
        for j in range(1, N-1):
            sx, sy = i, j
            for k in range(1, 5):
                nx = sx + dx[k]
                ny = sy + dy[k]
                # 현재 미생물이 존재하고 가고자 하는 행이 비어있을 때
                if arr[sx][sy][0] and arr[nx][ny][0] == 0:
                    # 이동방향이 일치할 때 ( 상 하 좌 우)
                    if k == arr[sx][sy][1]:
                        # 근데 약을 밟으면 반토막
                        if nx == 0 or ny == 0:
                            arr[nx][ny][0] += int(arr[sx][sy][0]/2)
                            arr[nx][ny][1] = arr[sx][sy][1]
                            arr[sx][sy] = [0, 0]
                        # 안밝으면 그대로
                        else:
                            arr[nx][ny][0] += arr[sx][sy][0]
                            arr[nx][ny][1] = arr[sx][sy][1]
                            arr[sx][sy] = [0, 0]
                print_arr()



                # 현재 미생물이 존재하고 가고자 하는 셀에 다른 미생물이 있을 때

