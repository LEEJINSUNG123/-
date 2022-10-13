import sys; sys.stdin = open('이진탐색.txt')

def preorder(n):
    global cnt
    if n <= N:
        preorder(2 * n)
        arr[n] = cnt
        cnt += 1
        preorder(2 * n + 1)

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    tree = [0] + [i for i in range(1, N+1)]
    arr = [0] * (N+1)
    cnt = 1
    preorder(1)
    print(f'#{tc} {arr[1]} {arr[N//2]}')
