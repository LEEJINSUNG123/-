import sys; sys.stdin = open('이진탐색_input.txt')

def inorder(n):
    global idx
    if n <= N:
        inorder(n * 2)
        tree[n] = idx
        idx += 1
        inorder(n * 2 + 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    tree = [0] * (N+1)
    idx = 1
    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N // 2]}')