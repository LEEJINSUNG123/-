import sys; sys.stdin = open('전기버스2_input.txt')

def dfs(n, k, e, cnt):
    global ans
    if ans <= cnt: return

    if n == k:
        if ans > cnt:
            ans = cnt
    else:
        # 충전O
        dfs(n, k+1, arr[k] - 1, cnt + 1)
        # 충전X
        if e > 0:
            dfs(n, k+1, e - 1, cnt)

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    ans = 987654321
    dfs(arr[0], 2, arr[1] - 1, 0)
    print(f'#{tc} {ans}')