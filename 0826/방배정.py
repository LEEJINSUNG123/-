import sys; sys.stdin = open('방배정.txt')

N, K = map(int, input().split())
arr = [[0] * 2 for _ in range(7)]

for i in range(N):
    S, Y = map(int, input().split())
    arr[Y][S] += 1

total = 0
for x in range(1,7):
    for y in range(2):
        while 1:
            if arr[x][y] == 0:
                break
            arr[x][y] -= K
            total += 1
            if arr[x][y] <= 0:
                break
print(total)



