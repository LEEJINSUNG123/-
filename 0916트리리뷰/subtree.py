import sys; sys.stdin = open('subtree.txt')

def preorder(n):
    global cnt
    if n:
        cnt += 1
        preorder(ch1[n])
        preorder(ch2[n])


t = int(input())
for tc in range(1, t+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    ch1 = [0] * (E + 2)
    ch2 = [0] * (E + 2)
    for i in range(E):
        p, c = arr[2*i], arr[2*i+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
    # print(ch1, ch2)
    cnt = 0
    preorder(N)
    print(f'#{tc} {cnt}')

    # [0, 6, 1, 0, 0, 3, 4][0, 0, 5, 0, 0, 0, 0]
    # [0, 0, 6, 0, 1, 3, 4][0, 0, 0, 0, 0, 0, 5]
    # [0, 0, 0, 0, 11, 3, 9, 6, 1, 5, 0, 8][0, 0, 0, 0, 0, 2, 0, 4, 10, 0, 0, 0]