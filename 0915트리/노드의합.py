import sys; sys.stdin = open('노드의합.txt')

t = int(input())
for tc in range(1, t+1):
    N, M, L = map(int, input().split())
    arr = [0] * (N+1)
    for _ in range(M):
        idx, val = map(int, input().split())
        arr[idx] = val
    for i in range(N-M, 0, -1):
        if N >= 2*i+1:
            arr[i] = arr[2*i] + arr[2*i+1]
        else:
            arr[i] = arr[2 * i]
    print(f'#{tc} {arr[L]}')



