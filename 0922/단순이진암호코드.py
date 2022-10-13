import sys; sys.stdin = open('단순이진암호코드.txt')

code = [[[[[[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)] \
          for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)]

code[0][0][0][1][1][0][1] = 0 # 0
code[0][0][1][1][0][0][1] = 1  # 1
code[0][0][1][0][0][1][1] = 2 # 2
code[0][1][1][1][1][0][1] = 3 # 3
code[0][1][0][0][0][1][1] = 4
code[0][1][1][0][0][0][1] = 5
code[0][1][0][1][1][1][1] = 6
code[0][1][1][1][0][1][1] = 7
code[0][1][1][0][1][1][1] = 8
code[0][0][0][1][0][1][1] = 9

def print_arr():
    for i in range(N):
        print(arr[i])

def find_pos(arr):
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == 1:
                return (i, j)

t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    # print_arr()
    # 시작위치찾기 = 뒤에서 1 찾기.
    sx, sy = find_pos(arr)
    # 시작위치로 이동.
    for i in range(8):
        sy -= 7
    sy += 1
    # 암호 찾기
    pwd_code = []   # 암호코드
    for i in range(8):
        pwd_code.append(
            code[arr[sx][sy]][arr[sx][sy+1]][arr[sx][sy+2]][arr[sx][sy+3]][arr[sx][sy+4]][arr[sx][sy+5]][arr[sx][sy+6]]
        )
        sy += 7
    # 검증
    pwd_verifi = (pwd_code[0] + pwd_code[2] + pwd_code[4] + pwd_code[6]) * 3 + pwd_code[1] + pwd_code[3] + pwd_code[5] + pwd_code[7]
    # 출력
    print(f'#{tc}', end=' ')
    if pwd_verifi % 10:
        print(0)
    else:
        print(sum(pwd_code))
