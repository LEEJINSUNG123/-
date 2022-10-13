import sys; sys.stdin = open('이진수1_input.txt')

hex = [
    [0, 0, 0, 0],   # 0
    [0, 0, 0, 1],   # 1
    [0, 0, 1, 0],   # 2
    [0, 0, 1, 1],   # 3
    [0, 1, 0, 0],   # 4
    [0, 1, 0, 1],   # 5
    [0, 1, 1, 0],   # 6
    [0, 1, 1, 1],   # 7
    [1, 0, 0, 0],   # 8
    [1, 0, 0, 1],   # 9
    [1, 0, 1, 0],   # A
    [1, 0, 1, 1],   # B
    [1, 1, 0, 0],   # C
    [1, 1, 0, 1],   # D
    [1, 1, 1, 0],   # E
    [1, 1, 1, 1]    # F
]

def hex_to_dec(c):
    if c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10

def make_bin(x):
    for i in range(4):
        bin.append(hex[x][i])

T = int(input())
for tc in range(1, T+1):
    n, arr = input().split()
    bin = []
    for i in range(len(arr)):
        make_bin(hex_to_dec(arr[i]))
    print(f"#{tc} {''.join(map(str, bin))}")
