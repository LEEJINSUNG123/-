import sys; sys.stdin = open('자기방으로돌.TXT')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    C = [0] * 200
    V = []
    for i in range(N):
        S, E = map(int, input().split())
        V.append(S)
        V.append(E)
        if S == E:
            pass
        elif S < E: # 1 400
            if S % 2 and E % 2 == 0:
                for q in range(S//2, E//2):
                    C[q] += 1
            elif S % 2 and E % 2:
                for q in range(S//2, (E//2)+1):
                    C[q] += 1
            elif S % 2 == 0 and E % 2 == 0:
                for q in range((S//2)-1, E//2):
                    C[q] += 1
            elif S % 2 == 0 and E % 2:
                for q in range((S//2)-1, (E//2)+1):
                    C[q] += 1

        else:   # 400 1
            if S % 2 and E % 2 == 0:
                for q in range((E // 2)-1, (S // 2)+1):
                    C[q] += 1
            elif S % 2 and E % 2:
                for q in range(E // 2, (S // 2) + 1):
                    C[q] += 1
            elif S % 2 == 0 and E % 2 == 0:
                for q in range((E // 2)-1, S // 2):
                    C[q] += 1
            elif S % 2 == 0 and E % 2:
                for q in range(E // 2, S // 2):
                    C[q] += 1
    print(f'#{tc} {max(C)}')

