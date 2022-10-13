import sys; sys.stdin = open('암호코드스캔.txt')

def print_arr():
    for i in range(N):
        print(arr[i])

table = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }

scan = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
    3211 : 0,
    2221 : 1,
    2122 : 2,
    1411 : 3,
    1132 : 4,
    1231 : 5,
    1114 : 6,
    1312 : 7,
    1213 : 8,
    3112 : 9,
    '3211' : 0,
    '2221' : 1,
    '2122' : 2,
    '1411' : 3,
    '1132' : 4,
    '1231' : 5,
    '1114' : 6,
    '1312' : 7,
    '1213' : 8,
    '3112' : 9,
    '211' : 0,
    '221' : 1,
    '122' : 2,
    '411' : 3,
    '132' : 4,
    '231' : 5,
    '114' : 6,
    312 : 7,
    '213' : 8,
    112 : 9
}

scan2 ={
    3211 : 0,
    2221 : 1,
    2122 : 2,
    1411 : 3,
    1132 : 4,
    1231 : 5,
    1114 : 6,
    1312 : 7,
    1213 : 8,
    3112 : 9,
    211 : 0,
    221 : 1,
    122 : 2,
    411 : 3,
    132 : 4,
    231 : 5,
    114 : 6,
    312 : 7,
    213 : 8,
    112 : 9
}

t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    temp = [input() for _ in range(N)]
    arr = [[] for _ in range(N)]
    print(f'#{tc} ******************************************************************************')
    # 2진수로 입력 받기
    for i in range(N):
        S = ''
        for j in range(M):
            S += table[temp[i][j]]
            arr[i] = S


    # 암호들 가져오기
    flag = False
    pw_list = []
    for i in range(1, N-1):
        for j in range(M*4-1, 0, -1):
            if arr[i][j] != '0' and arr[i-1][j] == '0':
                pw_list.append((i, j))
                break
    # print(pw_list)

    cnt = 0
    result = [[] for _ in range(len(pw_list))]

    idx = 0
    for x, y in pw_list:
        # print(x, y)
        cnt_one = 0
        cnt_zero = 0
        flag = True
        k = ''
        for j in range(y, 0, -1):
            if arr[x][j] == '1':
                if not flag:
                    result[idx].append(cnt_zero)
                    cnt_zero = 0
                cnt_one += 1
                flag = True
            else:
                if flag:
                    result[idx].append(cnt_one)
                    cnt_one = 0
                cnt_zero += 1
                flag = False
        idx += 1
    for i in range(len(result)):
        result[i].reverse()
    print(result)
    password_l = []
    for i in range(len(result)):
        if len(result[i]) == 31:
            password_l.append(result[i])
        else:
            for j in range(len(result[i])//31):
                password_l.append(result[x:x+31])
    print(password_l)
    # min_v = 0
    # for i in range(len(password_l)):
    #     if len(password_l[i]) >= 1:
    #         min_v = min(password_l[i])
    #         for j in range(len(password_l[i])):
    #             password_l[i][j] //= min_v
    #     else:
    #         print(f'{tc} 0')
    #         break

    # password_l = list(set(password_l))




