import sys
sys.stdin = open("1209_Sum_input.txt")

T = 10 # 테스트케이스 갯수
for tc in range(1, T+1):
    no = int(input())
    N = 100  # 배열의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0   # 정답
    # 행우선
    for i in range(N):
        total = 0
        for j in range(N):
            total += arr[i][j]
        # 최대값 변경
        if max_value < total:
            max_value = total

    # 열우선
    for i in range(N):
        total = 0
        for j in range(N):
            total += arr[j][i]
        # 최대값 변경
        if max_value < total:
            max_value = total

    # 대각선 \
    total = 0
    for i in range(N):
        total += arr[i][i]
    # 최대값 변경
    if max_value < total:
        max_value = total

    # 대각선 /
    total = 0
    for i in range(N):
        total += arr[i][N-1-i]
    # 최대값 변경
    if max_value < total:
        max_value = total

    print(f'#{tc} {max_value}')