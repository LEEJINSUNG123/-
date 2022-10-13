import sys; sys.stdin = open("파스칼.txt","r")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = []


    for i in range(1, n+1):
        arr.append([0]*i)


    for i in range(n):
        arr[i][0] = 1
        arr[i][-1] = 1
    if n > 1:
        arr[2][1] = 2

    for i in range(3, n):
        for j in range(1, i):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(f'#{tc}')

    for i in arr:
        for j in i:
            print(j, end=' ')
        print()