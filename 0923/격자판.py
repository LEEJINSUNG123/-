import sys; sys.stdin = open('격자판.txt')

# def bfs(x,y):
#     Q = []
#     Q.append((x,y))
#     # s += str(arr[x][y])
#     s = ''
#     visited[x][y] = 1
#
#     while Q:
#         x, y = Q.pop(0)
#         s += str(arr[x][y])
#         for i in range(4):
#             print(visited[i])
#         print(s)
#         if len(s) >= 7:
#             s_list.add(s)
#             s = ''
#             return
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < 4 and 0 <= ny < 4:
#                 if not visited[nx][ny]:
#                     visited[nx][ny] += visited[x][y]
#                     Q.append((nx, ny))

def dfs(x, y, s):
    if len(s) > 7:
        return
    if len(s) == 7:
        s_list.add(s)
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4:
                dfs(nx, ny, s+arr[nx][ny])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
T = int(input())
for tc in range(1, T+1):
    arr = [list(map(str, input().split())) for _ in range(4)]
    # visited = [[0] * 4 for _ in range(4)]
    s_list = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])
    # print(s_list)
    print(f'#{tc} {len(s_list)}')
