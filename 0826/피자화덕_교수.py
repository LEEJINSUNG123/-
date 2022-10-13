import sys; sys.stdin = open('피자화덕.txt')

def pizza():
    Q = []
    for i in range(1, N+1): # 화덕에 N개 피자 넣기
        Q.append(i)

    idx = N + 1
    while len(Q) > 1:
        t = Q.pop(0)
        arr[t] = arr[t] // 2
        # 치즈가 남아 있으면
        if arr[t] != 0:
            Q.append(t)
        # 치즈가 다 녹았을 때
        elif idx <= M:
            Q.append\
                (idx)
            idx += 1

    return Q[0]


T = int(input())
for tc in range(1, T+1):
    N, M = map(int ,input().split())
    arr = [0] + list(map(int, input().split()))
    print(f'#{tc} {pizza()}')