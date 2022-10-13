import sys; sys.stdin = open("회문.txt")

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]

    c = m//2
    flag = 0
    # garo
    if m % 2:
        for i in arr:
            for j in range(n-m+1):
                cnt = 0
                Str = i[j:j+m]
                for k in range(1, m//2+1):
                    if Str[c-k] == Str[c+k]:
                        cnt += 1
                if cnt == c:
                    flag = 1
                    result = Str
    else:
        for i in arr:
            for j in range(n-m+1):
                cnt = 0
                Str = i[j:j+m]
                for k in range(m//2):
                    if Str[c-k-1] == Str[c+k]:
                        cnt += 1
                if cnt == c:
                    flag = 1
                    result = Str
    # sero
    new_arr = []

    for i in range(n):
        new_str = ''
        for j in range(n):
            new_str += arr[j][i]
        new_arr.append(new_str)

    if m % 2:
        for i in new_arr:
            for j in range(n-m+1):
                cnt = 0
                Str = i[j:j+m]
                for k in range(1, m//2+1):
                    if Str[c-k] == Str[c+k]:
                        cnt += 1
                if cnt == c:
                    flag = 1
                    result = Str
    else:
        for i in new_arr:
            for j in range(n-m+1):
                cnt = 0
                Str = i[j:j+m]
                for k in range(m//2):
                    if Str[c-k-1] == Str[c+k]:
                        cnt += 1
                if cnt == c:
                    flag = 1
                    result = Str
    if flag == 1:
        print(f'#{tc} {result}')
