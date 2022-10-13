import sys; sys.stdin = open("샘숭버스.txt")

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    bus = [0]
    # 노선 범위
    for _ in range(N):
        min ,max = map(int, input().split())
        bus.append(min)
        bus.append(max)
    # 노선 개수 카운트 딕셔너리
    P = int(input())
    C = []
    for _ in range(P):
        c = int(input())
        C.append(c)
    cnt_dict = {}
    for c in C:
        cnt_dict[c] = 0
    # 노선 카운트
    for i in range(1, N+1):
        for cnt in range(bus[2*i-1], bus[2*i]+1):
            for key in cnt_dict.keys():
                if key == cnt:
                    cnt_dict[key] += 1

    print(f'#{tc}', end=' ')
    for key in C:
        print(cnt_dict[key], end=' ')
    print()


