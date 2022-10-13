import sys
sys.stdin = open('붕어빵.txt')

T = int(input())
for t in range(1, T+1):
    print(f'#{t}', end=' ')
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    flag = 1
    cnt = 0
    save = 0
    if arr[0] < M:
        flag = 0
    for i in range(1, N):  # 1
        if arr[0] < M:
            flag = 0
            break
        else:
            if M * i < arr[i] < M * (i+1):
                save += K
                cnt += 1
                if cnt > save:
                    flag = 0
                    break
                save -= cnt

    if flag:
        print('Possible')
    else:
        print('Impossible')