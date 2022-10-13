import sys; sys.stdin = open('이진수2_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    s = ''
    cnt = 0
    print(f'#{tc}', end=' ')
    while N != 0 and cnt < 13:
        N *= 2
        cnt += 1
        if N >= 1:
            s += '1'
            N -= 1
        else:
            s += '0'
    if cnt <= 12:
        print(s)
    else:
        print('overflow')
