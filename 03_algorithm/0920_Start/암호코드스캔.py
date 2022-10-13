import sys; sys.stdin = open('암호코드스캔_input.txt')
p = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9
}

hex_to_bin = {
    '0': [0, 0, 0, 0], '1': [0, 0, 0, 1], '2': [0, 0, 1, 0], '3': [0, 0, 1, 1],
    '4': [0, 1, 0, 0], '5': [0, 1, 0, 1], '6': [0, 1, 1, 0], '7': [0, 1, 1, 1],
    '8': [1, 0, 0, 0], '9': [1, 0, 0, 1], 'A': [1, 0, 1, 0], 'B': [1, 0, 1, 1],
    'C': [1, 1, 0, 0], 'D': [1, 1, 0, 1], 'E': [1, 1, 1, 0], 'F': [1, 1, 1, 1],
}

def solve():
    ans = 0
    for i in range(N):   # 행
        j = M * 4 - 1    # 열(마지막index)
        while j >= 55:
            if arr[i][j] == 1 and arr[i-1][j] == 0:
                pwd = []
                for _ in range(8):
                    c2 = c3 = c4 = 0
                    while arr[i][j] == 1:
                        c4 += 1
                        j -= 1
                    while arr[i][j] == 0:
                        c3 += 1
                        j -= 1
                    while arr[i][j] == 1:
                        c2 += 1
                        j -= 1
                    while arr[i][j] == 0:
                        j -= 1
                    MIN = min(c2, c3, c4)
                    pwd.append(p[(c2//MIN, c3//MIN, c4//MIN)])
                odd = pwd[0] + pwd[2] + pwd[4] + pwd[6]
                even = pwd[1] + pwd[3] + pwd[5] + pwd[7]
                if(even * 3 + odd) % 10 == 0:
                    ans += even + odd
                j += 1
                # 같은 행에 암호코드 블럭이 겹쳐 있다면 다음 암호 블럭에 도착
                # j를 오른쪽으로 한 칸 이동해야함(아래에서 j가 감소되기 때문)
            j -= 1
    return ans

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N)]
    for i in range(N):
        tmp = input()                       # 16진수 받아서
        for j in range(M):
            arr[i] += hex_to_bin[tmp[j]]    # 2진수로 변환
    print(f'#{tc} {solve()}')