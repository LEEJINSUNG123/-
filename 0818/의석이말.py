import sys; sys.stdin = open("의석이말.txt")

t = int(input())
for tc in range(1, t+1):
    arr = [list(map(str, input())) for _ in range(5)]
    # 문자열 최대 길이
    max_len = 0
    for i in range(5):
        if max_len < len(arr[i]):
            max_len = len(arr[i])
    # 짧은문자열 채우기
    for j in range(5):
        c = len(arr[j])
        if c < max_len:
            for k in range(max_len-c):
                arr[j].append('*')

    print(f'#{tc}', end= ' ')
    for i in range(max_len):
        for j in range(5):
            if arr[j][i] != '*':
                print(arr[j][i], end= '')
    print()

