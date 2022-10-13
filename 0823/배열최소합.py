import sys; sys.stdin = open("배열최소합.txt")

def perm(n, k, ssum): # , ssum
    # 가지치기 현재까지 더한게 크다.
    global ans
    # if ans < ssum:
    #     break


    if k == n:
        print(arr)
        # ans = xxx
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1, ssum)
            arr[k], arr[i] = arr[i], arr[k]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arrr = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        arr = arrr[i]
        perm(n, 0, 0)
