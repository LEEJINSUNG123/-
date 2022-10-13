import sys; sys.stdin = open('홈방법서비스.txt')

# 마름모
def thin_mo(s,e):
    count = 0
    if s - (k - 1) >= 0:
        s = s - (k - 1)
    else:
        s = 0
    for i in range(1, 2*k):
        cnt = i
        if cnt > k:
            for j in range(k-(cnt-k+1), -1, -1):
                if 0 <= s < N and 0 <= e + j <= N and 0 <= e - j <= N:
                    # if arr[s][e + j] == 1:
                    #     count += 1
                    # if arr[s][e - j] == 1:
                    #     count += 1
                    arr[s][e + j] = 5

                    arr[s][e - j] = 5

        else:
            for j in range(cnt):
                if 0 <= s < N and 0 <= e + j <= N and 0 <= e - j <= N:
                    # if arr[s][e + j] == 1:
                    #     count += 1
                    # if arr[s][e - j] == 1:
                    #     count += 1
                    arr[s][e + j] = 5

                    arr[s][e - j] = 5
        s += 1
    return count

t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    k = 1
    fee = k * k + (k - 1) * (k - 1)
    # s,e = 0, 0
    print(thin_mo(4,3))
    for i in range(N):
        print(arr[i])