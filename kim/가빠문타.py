import sys; sys.stdin = open("가빠문타.txt")

t = int(input())
for tc in range(1, t+1):
    a, b = map(str, input().split())
    n = len(a) # text
    m = len(b)
    cnt = i = 0

    # for i in range(n-m+1):
    while i < n-m+1:
        flag = 1
        for j in range(m):
            if a[i+j] != b[j]:
                flag = 0
                break
        if flag:
            i += m
            cnt += 1
        else:
            i += 1

        # if flag:
        #     cnt += 1
        #     i += m - 1
        # i += 1
        # print(i)

    # print(cnt)
    print(f'#{tc} {n-m * cnt + cnt}')