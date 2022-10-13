import sys; sys.stdin = open('디저트카페.txt')

def dfs(x, y, dir, cnt):
    global result
    nx = x + dx[dir]
    ny = y + dy[dir]
    # 출발점에 도착하면
    if nx == sx and ny == sy:
        result = max(result, cnt)
        return
    # 인덱스체크, 방문체크
    if 0 <= nx < N and 0 <= ny < N and visited[arr[nx][ny]] == 0:
        visited[arr[nx][ny]] = 1
        dfs(nx, ny, dir, cnt + 1)   # 직진
        # 방향전환
        if dir < 3:
            dfs(nx, ny, dir + 1, cnt + 1)
        visited[arr[nx][ny]] = 0

#   우하 좌하 좌상 우상
dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 메뉴(번호)
    visited = [0] * 101
    result = -1

    for i in range(N):
        for j in range(N):
            sx, sy = i, j   # 출발점 체크 / 도착을 확인하기 위해
            visited[arr[i][j]] = 1
            dfs(i, j, 0, 1)
            visited[arr[i][j]] = 0 # 다른방향으로 갈 수 있게 해제

    print(f'#{tc} {result}')