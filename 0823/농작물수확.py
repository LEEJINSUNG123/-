import sys; sys.stdin = open("농작물수확.txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    center = len(arr) // 2
    total = 0
    if n == 1:
        total = arr[0][0]
        print(f'#{tc} {total}')
        continue
    else:
        total = arr[0][center] + arr[n-1][center]
        for i in range(1, center+1):
            total += sum(arr[i][center-i:center+i+1])

        k = center - 1
        for j in range(center+1, n-1):
            total += sum(arr[j][center-k:center+k+1])
            k -= 1
        print(f'#{tc} {total}')
