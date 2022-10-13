import sys; sys.stdin = open('전기버스2.txt')

def drive(x, cnt):  # 출발 정류장, 충전 횟수
    global ans
    if cnt >= ans:
        return
    if arr[x] + x >= N:
        if ans > cnt:
            ans = cnt
        return
    else:
        for i in range(1, arr[x]+1):
            drive(x+i, cnt + 1)

t = int(input())
for tc in range(1, t+1):
    arr =[0] + list(map(int, input().split()))
    N = arr.pop(1)  # 정류장 수
    station = [i for i in range(1, N+1)]
    ans = N
    cnt = 0
    print(arr)
    print(station)
    drive(1, 0)
    print(f'#{tc} {ans}')