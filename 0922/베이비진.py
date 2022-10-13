import sys; sys.stdin = open('베이비진.txt')

t = int(input())
for tc in range(1, t+1):
    arr = [0] + list(map(int, input().split()))
    p1_count = [0] * 10
    p2_count = [0] * 10
    flag = result = 0
    for i in range(1, 13):
        # 입력
        if i % 2:
            p1_count[arr[i]] += 1
        else:
            p2_count[arr[i]] += 1
        # babygin 확인
        for j in range(10):
            if p1_count[j] >= 3:
                result = 1
                flag = 1
                break
            if p2_count[j] >= 3:
                result = 2
                flag = 1
                break
        for p in range(8):
            if p1_count[p] >= 1 and p1_count[p+1] >= 1 and p1_count[p+2] >= 1:
                result = 1
                flag = 1
                break
            if p2_count[p] >= 1 and p2_count[p+1] >= 1 and p2_count[p+2] >= 1:
                result = 2
                flag = 1
                break
        if flag:
            break
    print(f'#{tc} {result}')