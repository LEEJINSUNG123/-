def dfs(idx, key, k, s):
    visited[idx] = 1
    cnt1 = cnt2 = 0
    if k == L-1:
        for i in s:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                cnt1 += 1
            else:
                cnt2 += 1
        if cnt1 >= 1 and cnt2 >= 2:
            print(s)
            return
    else:
        for i in range(C):
            if visited[i] == 0 and ord(arr[i]) > key:
                visited[i] = 1
                dfs(i, ord(arr[i]), k+1, s + arr[i])
                visited[i] = 0

L, C = map(int, input().split())
arr = list(input().split())

for i in range(C):
    arr[i] = ord(arr[i])
arr.sort()

for i in range(C):
    arr[i] = chr(arr[i])
visited = [0] * C
for i in range(C):
    dfs(i, ord(arr[i]), 0, arr[i])