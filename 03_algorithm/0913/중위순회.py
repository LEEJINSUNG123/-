import sys; sys.stdin = open('중위순회_input.txt')

def inorder(n):
    if n <= N:
        inorder(2*n)
        print(tree[n], end='')
        inorder(2*n+1)

T = 10
for tc in range(1, T+1):
    N = int(input())    #정점수
    tree = [''] * (N+1)
    for i in range(N):
        temp = list(input().split())
        idx = int(temp[0])
        tree[idx] = temp[1]

    print(f'#{tc}', end=' ')
    inorder(1)
    print()