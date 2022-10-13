import sys; sys.stdin = open('이진수2.txt')

hex = [
    [0, 0, 0, 0, ], # 0
    [0, 0, 0, 1, ], # 1
    [0, 0, 1, 0, ], # 2
    [0, 0, 1, 1, ], # 3
    [0, 1, 0, 0, ],
    [0, 1, 0, 1, ],
    [0, 1, 1, 0, ],
    [0, 1, 1, 1, ],
    [1, 0, 0, 0, ],
    [1, 0, 0, 1, ],
    [1, 0, 1, 0, ],
    [1, 0, 1, 1, ],
    [1, 1, 0, 0, ],
    [1, 1, 0, 1, ],
    [1, 1, 1, 0, ],
    [1, 1, 1, 1, ],
]

def hex_to_dec(c):
    if c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10

def make_bin(x):
    for i in range(4):
        bin.append(hex[x][i])

t = int(input())
for tc in range(1, t+1):
    N = float(input())
    s = ''
    cnt = 0
    # print(f'#{tc}', end=' ')
    while N != 0 and cnt <= 12:
        N *= 2
        cnt += 1
        if N >= 1:
            s += '1'
            N -= 1
        else:
            s += '0'

    if cnt <= 12:
        print(f'#{tc} {s}')
    else:
        print(f'#{tc} overflow')

