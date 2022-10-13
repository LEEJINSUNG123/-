import sys; sys.stdin = open("원재메모리복구.txt")

t = int(input())
for tc in range(1, t+1):
    str1 = list(input())
    cnt = 0
    if str1[-1] == '0':
        for i in range(len(str1)-1,0,-1):
            if str1[i] != str1[i-1]:
                cnt += 1
        if str1[0] == '1':
            cnt += 1

    elif str1[-1] == '1':
        for i in range(len(str1)-1,0,-1):
            if str1[i] != str1[i-1]:
                cnt += 1
        if str1[0] == '1':
            cnt += 1
    print(f'#{tc} {cnt}')