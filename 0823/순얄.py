import sys; sys.stdin = open("배열최소합.txt")

def perm(n, k, ssum):

    global ans
    if ans < ssum:
        break

    if k == n:
        print(arr)
        ans = 0
        x = 0
        for i in arr:
            ans += arrr[x][i-1]
            x += 1
        print(ans)

    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1, ssum)
            arr[k], arr[i] = arr[i], arr[k]


t = int(input())
for tc in range(1, t+1):
    ans = 0
    arr = [1, 2, 3]
    n = len(arr)

    N = int(input())
    arr = []
    for i in range(1, N+1):
        arr.append(i)
    print(arr)
    arrr = [list(map(int, input().split())) for _ in range(N)]
    perm(n, 0, 0)
