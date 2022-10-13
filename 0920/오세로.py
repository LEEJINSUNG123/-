# import sys; sys.stdin = open('오셀로.txt')
#
# def print_arr():
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             print(arr[i][j], end=' ')
#         print()
#
# def check(sx, sy, dol):
#     for i in range(8):
#         # sx와 sy를 시작점으로 기억해야함.
#         nx = sx + dx[i]
#         ny = sy + dy[i]
#         flag = False
#         # 벽이 아니면 주어진 방향으로 계속 증가
#         while 0 < nx <= N and 0 < ny <= N:
#             # 0 이면 break
#             if arr[nx][ny] == 0:
#                 break
#             # 같은 돌, flag체크 ex, ey 변경
#             if arr[nx][ny] == dol:
#                 flag = True
#                 ex = nx
#                 ey = ny
#                 break # 가까운 위치의 같은 색상의 돌을 찾고 그만
#             nx += dx[i]
#             ny += dy[i]
#
#         # flag가 True이면
#         if flag:
#             nx = sx
#             ny = sy
#             while not(nx == ex and ny == ey):
#                 nx += dx[i]
#                 ny += dy[i]
#                 arr[nx][ny] = dol
#
#
#
# dx = [-1, -1, 0, 1, 1, 1, 0, -1]
# dy = [0, 1, 1, 1, 0, -1, -1, -1]
#
# t = int(input())
# for tc in range(1, t+1):
#     N, M = map(int, input().split())
#     arr = [[0] * (N+1) for _ in range(N+1)]
#
#     # 초기화
#     mid = N // 2
#     arr[mid][mid] = arr[mid+1][mid+1] = 2
#     arr[mid+1][mid] = arr[mid][mid + 1] = 1
#     # print_arr()
#
#     # 돌놓기
#     for i in range(M):
#         x, y, dol = map(int, input().split())
#         arr[x][y] = dol
#         check(x, y, dol)
#         # print_arr()
#         # print()
#
#     # 돌세기
#     B = 0
#     W = 0
#     for i in range(1,N+1):
#         for j in range(1, N+1):
#             if arr[i][j] == 1: B += 1
#             if arr[i][j] == 2: W += 1
#
#     print(f'#{tc} {B} {W}')
#
#
print(len([2, 1, 1, 1, 3, 1, 2, 1, 3, 1, 2, 1, 1, 3, 2, 1, 4, 1, 1, 2, 2, 2, 1, 1, 4, 1, 1, 3, 1, 1, 2]))
print(len('01F8FF8E00FC7E00E3F0070071F81F81C7007E0703F000000000'))