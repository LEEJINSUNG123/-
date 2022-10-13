import sys; sys.stdin = open('수영장.txt')

T = int(input())
for tc in range(1, T+1):
    d, m, mmm, y = map(int, input().split())
    date = list(map(int, input().split()))
    fare = [0] * 12
    # 1일 1월 비교
    for i in range(len(date)):
        if date[i] == 0:
            fare[i] = 0
        else:
            # 1일권 가격
            d_fare = d * date[i]
            # 1개월 가격이 1일권 가격들보다 싸면 월권
            if d_fare > m:
                fare[i] = m
            else:
                fare[i] = d_fare
    if sum(fare) <= mmm and sum(fare) <= y:
        print(f'#{tc} {sum(fare)}')
    # 1개월 3개월 비교
    for i in range(len(date)):
        if date[i] == 0:
            fare[i] = 0
        else:


    print(fare)
