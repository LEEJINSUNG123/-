import sys; sys.stdin = open('미생물격리_input.txt')

def solve():
    for _ in range(M):
        # 1. 미생물 이동, 경계 처리
        for i in range(len(arr)):
            arr[i][0] = arr[i][0] + dx[arr[i][3]] # x좌표
            arr[i][1] = arr[i][1] + dy[arr[i][3]]  # y좌표

            # 벽만나면
            if arr[i][0] == 0 or arr[i][0] == N-1 \
                or arr[i][1] == 0 or arr[i][1] == N-1:
                arr[i][2] //= 2
                arr[i][3] = opp[arr[i][3]]
        # 2. 정렬(좌표, 개체수) 내림차순
        arr.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)

        # 3. 같은좌표 -> 큰개체에 합산후 제거
        i = 1
        while i < len(arr):
            # 위의 미생물과 비교
            if arr[i-1][0] == arr[i][0] and arr[i-1][1] == arr[i][1]:
                arr[i-1][2] += arr[i][2]
                arr.pop(i)
            else:
                i += 1


dx = [0, -1, 1, 0, 0]   # 상하좌우
dy = [0, 0, 0, -1, 1]
opp = [0, 2, 1, 4, 3]   # 반대방향
T = int(input())
for tc in range(1, T+1):
    # 크기, 시간, 개체수
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(K)]

    solve()
    ans = 0
    for i in range(len(arr)):
        ans += arr[i][2]
    print(f'#{tc} {ans}')