import sys; sys.stdin = open('회문.txt')

def f(arr):
    m = 100 # 회문 최대길이
    for i in range(n):
        for j in range(n - m + 1):
            flag = 1
        for k in range(m // 2):
            if arr[i][j + k] != arr[i][j + m - 1 - k]:
                flag = 0
        break
    # 출력
        if flag:
            for k in range(m):
                print(f'{arr[i][j + k]}', end='')
            print()

    for i in range(n):
        for j in range(n - m + 1):
            flag = 1
            for k in range(m // 2):
                if arr[j + k][i] != arr[j + m - 1 - k][i]:
                    flag = 0
                    break
            # 출력
        if flag:
            for k in range(m):
                print(f'{arr[j + k][i]}', end='')
            print()
    m -= 1

t = int(input())
for tc in range(1, 1+t):
    n, m = 100, 100
    no = int(input())
    arr = [list(input()) for _ in range(n)]

    print(f'#{tc}', end =' ')
