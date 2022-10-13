import sys; sys.stdin = open("test.txt", "r")

def pal(word):
    return word == word[::-1]

size = 10
t = 1
for tc in range(1, t+1):
    temp = int(input())
    arr = [input() for _ in range(10)]

    # 세로 가로로 바꾸기
    new_arr = []
    for i in range(10):
        new_str = ''
        for j in range(10):
            new_str += arr[j][i]
        new_arr.append(new_str)
    print(new_arr)
    # 길이가 100인 거
    m = size
    max_l_s = 0
    while m > 0:
        for j in new_arr:
            for i in range(10 - m + 1):
                x = pal(j[i:i+m])
                if x:
                    if max_l_s < len(j[i:i+m]):
                        max_l_s = len(j[i:i+m])
        m -= 1

    m = size
    max_l_g = 0
    while m > 0:
        for j in arr:
            for i in range(10 - m + 1):
                x = pal(j[i:i+m])
                if x:
                    if max_l_g < len(j[i:i+m]):
                        max_l_g = len(j[i:i+m])
            m -= 1

    if max_l_s > max_l_g:
        print(f'#{tc} {max_l_s}')
    else:
        print(f'#{tc} {max_l_g}')
