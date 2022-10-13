import sys; sys.stdin = open("회문2.txt", "r")

def pal(word):
    return word == word[::-1]

size = 100
t = 10
for tc in range(1, t+1):
    temp = int(input())
    arr = [input() for _ in range(100)]

    # 세로 가로로 바꾸기
    new_arr = []
    for i in range(100):
        new_str = ''
        for j in range(100):
            new_str += arr[j][i]
        new_arr.append(new_str)

    m = size
    max_l_sero = max_l_garo = 0
    while m > 0:
        for j in range(100):
            for i in range(100 - m + 1):
                x = pal(arr[j][i:i + m])
                y = pal(new_arr[j][i:i+m])
                if x:
                    if max_l_garo < len(arr[j][i:i+m]):
                        max_l_garo = len(arr[j][i:i+m])
                if y:
                    if max_l_sero < len(new_arr[j][i:i+m]):
                        max_l_sero = len(new_arr[j][i:i+m])
        m -= 1

    if max_l_sero > max_l_garo:
        print(f'#{tc} {max_l_sero}')
    else:
        print(f'#{tc} {max_l_garo}')
