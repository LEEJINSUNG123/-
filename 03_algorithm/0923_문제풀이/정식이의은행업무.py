import sys; sys.stdin = open('정식이의은행업무_input.txt')

def to_dec(x, mode):
    value = 0
    for i in range(len(x)):
        value = value * mode + int(x[i])
    return value

def f():
    # 같은값 찾기
    for i in range(len(list2)):
        for j in range(len(list3)):
            if list2[i] == list3[j]:
                return list2[i]


T = int(input())
for tc in range(1, T+1):
    str2 = input()
    str3 = input()

    list2 = []      # 2진수를 10진수로 바꾼 결과 저장
    list3 = []      # 3진수를 10진수로 바꾼 결과 저장

    # 2진수
    for i in range(len(str2)):
        x2 = list(str2)
        x2[i] = str((int(x2[i]) + 1) % 2)
        list2.append(to_dec(x2, 2))

    # 3진수
    for i in range(len(str3)):
        for j in [1, 2]:
            x3 = list(str3)
            x3[i] = str((int(x3[i]) + j) % 3)
            list3.append(to_dec(x3, 3))

    print(f'#{tc} {f()}')






