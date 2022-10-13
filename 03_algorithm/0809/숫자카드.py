import sys; sys.stdin = open('숫자카드_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = int(input())
    # cnt = 0
    # while num:
    #     num //= 10
    #     cnt += 1
    # print(cnt)
    # 카운팅
    count = [0] * 10
    for i in range(N):
        count[num % 10] += 1
        num //= 10

    # 최대값의 인덱스
    max_idx = 0
    for i in range(1, 10):
        if count[max_idx] <= count[i]:
            max_idx = i

    print(f'#{tc} {max_idx} {count[max_idx]}')
