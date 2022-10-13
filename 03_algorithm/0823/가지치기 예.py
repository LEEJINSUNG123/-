def perm(n, k, ssum):
    global ans
    if ans < ssum:
        return

    if k == n:
        if ans > ssum:
            ans = ssum
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k + 1, ssum + ???)
            arr[k], arr[i] = arr[i], arr[k]


ans = 987654321
arr = [1, 2, 3]
N = len(arr)
perm(N, 0, 0)