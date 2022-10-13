# .	평지(전차가 들어갈 수 있다.)
# *	벽돌로 만들어진 벽
# #	강철로 만들어진 벽
# -	물(전차는 들어갈 수 없다.)
# ^	위쪽을 바라보는 전차(아래는 평지이다.)
# v	아래쪽을 바라보는 전차(아래는 평지이다.)
# <	왼쪽을 바라보는 전차(아래는 평지이다.)
# >	오른쪽을 바라보는 전차(아래는 평지이다.)

# U	Up : 전차가 바라보는 방향을 위쪽으로 바꾸고, 한 칸 위의 칸이 평지라면 위 그 칸으로 이동한다.
# D	Down : 전차가 바라보는 방향을 아래쪽으로 바꾸고, 한 칸 아래의 칸이 평지라면 그 칸으로 이동한다.
# L	Left : 전차가 바라보는 방향을 왼쪽으로 바꾸고, 한 칸 왼쪽의 칸이 평지라면 그 칸으로 이동한다.
# R	Right : 전차가 바라보는 방향을 오른쪽으로 바꾸고, 한 칸 오른쪽의 칸이 평지라면 그 칸으로 이동한다.
# S	Shoot : 전차가 현재 바라보고 있는 방향으로 포탄을 발사한다.

import sys; sys.stdin = open("상호의배필.txt")

t = int(input())
for tc in range(1, t+1):
    # 높이, 너비
    H, W = map(int, input().split())
    # 게임 맵
    arr = [list(map(str, input())) for _ in range(H)]
    # 사용자 커멘트 입력
    N = int(input())
    command_l = list(input())
    for i in range(H):
        print(arr[i])
    print(command_l)
    # 좌 우 하 상
    di = [0, 0, 1, -1]
    dj = [-1, 1, 0, 0]

    direction = {'left': 0, 'right': 1, 'down': 2, 'up': 3}
    key = ''

    for i in range(H):
        for j in range(W):
            if arr[i][j] == '<':
                key = 'left'
                pos_x, pos_y = i, j
            elif arr[i][j] == '^':
                key = 'up'
                pos_x, pos_y = i, j
            elif arr[i][j] == '>':
                key = 'right'
                pos_x, pos_y = i, j
            elif arr[i][j] == 'v':
                key = 'down'
                pos_x, pos_y = i, j
    print(key, pos_x, pos_y)

    # .	평지(전차가 들어갈 수 있다.)
    # *	벽돌로 만들어진 벽
    # #	강철로 만들어진 벽
    # -	물(전차는 들어갈 수 없다.)
    ni, nj = pos_x, pos_y
    # SRSSRRUSSR
    for x in range(len(command_l)):
        if command_l[x] == 'S':
            while pos_x >= 0 and pos_y >= 0 and pos_y <= W-1 and pos_x <= H-1:
                if key == 'up':
                    pos_x = pos_x - 1
                    pos_y = pos_y
                elif key == 'down':
                    pos_x = pos_x + 1
                    pos_y = pos_y
                elif key == 'left':
                    pos_x = pos_x
                    pos_y = pos_y - 1
                elif key == 'right':
                    pos_x = pos_x
                    pos_y = pos_y + 1

                # 포탄이 벽에 박을 때
                if pos_x >= 0 and pos_y >= 0 and pos_y <= W-1 and pos_x <= H-1:
                    if arr[pos_x][pos_y] == '*':
                        arr[pos_x][pos_y] = '.'
                        break
                    elif arr[pos_x][pos_y] == '#':
                        break

        elif command_l[x] == 'R':
            key = 'right'
            new_i, new_j = ni, nj+1
            if new_i >= 0 and new_j >= 0 and new_j <= W-1 and new_i <= H-1:
                if arr[new_i][new_j] == '.':
                    arr[ni][nj] = '.'
                    arr[new_i][new_j] = '>'
                    ni, nj = new_i, new_j
        elif command_l[x] == 'L':
            key = 'left'
            new_i, new_j = ni, nj - 1
            if new_i >= 0 and new_j >= 0 and new_j <= W - 1 and new_i <= H - 1:
                if arr[new_i][new_j] == '.':
                    arr[ni][nj] = '.'
                    arr[new_i][new_j] = '<'
                    ni, nj = new_i, new_j

        elif command_l[x] == 'U':
            key = 'up'
            new_i, new_j = ni-1, nj
            if new_i >= 0 and new_j >= 0 and new_j <= W - 1 and new_i <= H - 1:
                if arr[new_i][new_j] == '.':
                    arr[ni][nj] = '.'
                    arr[new_i][new_j] = '^'
                    ni, nj = new_i, new_j
        elif command_l[x] == 'D':
            key = 'down'
            new_i, new_j = ni+1, nj
            if new_i >= 0 and new_j >= 0 and new_j <= W - 1 and new_i <= H - 1:
                if arr[new_i][new_j] == '.':
                    arr[ni][nj] = '.'
                    arr[new_i][new_j] = 'v'
                    ni, nj = new_i, new_j
    for l in range(len(arr)):
        print(arr[l])
