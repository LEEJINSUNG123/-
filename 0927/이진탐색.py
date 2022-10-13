import sys; sys.stdin = open('이진탐색.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr_n = list(map(int, input().split()))
    arr_m = list(map(int, input().split()))
    arr_n.sort()
    cnt = 0
    find = []
    for key in arr_m:
        dir = 0
        l = 0
        r = N - 1
        mid = (l + r) // 2
        # 처음 탐색
        if key > arr_n[N-1]:
            continue
        if key == arr_n[mid]:
            cnt += 1
            find.append(key)
            continue
        elif key > arr_n[mid]:
            l = mid + 1
            dir = 2
        elif key < arr_n[mid]:
            r = mid - 1
            dir = 1
        while l <= r:
            mid = (l + r) // 2
            if key == arr_n[mid]:
                cnt += 1
                find.append(key)
                break
            elif key > arr_n[mid] and dir == 1:
                l = mid + 1
                dir = 2
            elif key < arr_n[mid] and dir == 2:
                r = mid - 1
                dir = 1
            else:
                break
    print(find)
    print(f'#{tc} {cnt}')



