import sys; sys.stdin = open('중위순위.txt')

def preorder(n):
    if n:
        preorder(ch1[n])
        print(alpah[n], end='')
        preorder(ch2[n])


for tc in range(1, 11):
    N = int(input())
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    alpah = [0] * (N + 1)

    for i in range(N):
        arr_v = list(input().split())
        if len(arr_v) == 4:
            alpah[int(arr_v[0])] = arr_v[1]
            ch1[int(arr_v[0])] = int(arr_v[2])
            ch2[int(arr_v[0])] = int(arr_v[3])
        elif len(arr_v) == 3:
            alpah[int(arr_v[0])] = arr_v[1]
            ch1[int(arr_v[0])] = int(arr_v[2])
        else:
            alpah[int(arr_v[0])] = arr_v[1]

    print(f'#{tc}', end=' ')
    preorder(1)
    print()
