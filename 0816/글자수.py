import sys; sys.stdin = open("글자수.txt", "r")

t = int(input())

for tc in range(1, t+1):
    str1 = set(input())
    str2 = input()
    str_dict = {}
    for s in str1:
        str_dict[s] = 0

    for i in str2:
        for key in str_dict.keys():
            if i == key:
                str_dict[key] += 1

    max_v = 0
    for key, value in str_dict.items():
        if max_v < value:
            max_v = value
            max_key = key
    print(f'#{tc} {str_dict[max_key]}')


