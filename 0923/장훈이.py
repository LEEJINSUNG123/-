import sys; sys.stdin = open('장훈이.txt')

def comb(n, r, ssum):
    pass

# T = int(input())
# for tc in range(1, T+1):
#     N, B = map(int, input().split())    # 점원 인원수, 탑의 높이
#     H = list(map(int, input().split())) # 점원의 키
#     ans = 0 # 높이의 차
#     T = [0] * N
#     print(f'#{tc} {ans}')

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    total = set()
    for i in range(1, 1 << N):  # 공집합은 제외,
        ans = 0
        for j in range(N):
            if i & (1 << j):
                ans += H[j]
        total.add(ans)
    total = list(total)
    total.sort()
    for k in total:
        if B <= k:
            print(f'#{tc} {k-B}')
            break
