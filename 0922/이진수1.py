import sys; sys.stdin = open('이진수1.txt')

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
    N, arr = input().split()
    bin = []
    for i in range(len(arr)):
        make_bin(hex_to_dec(arr[i]))
    print(bin)
    print(f'#{tc} {"".join(map(str, bin))}')