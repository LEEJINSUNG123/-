import sys; sys.stdin = open('이진수2.txt')

t = int(input())
for tc in range(1, t+1):
    N = float(input())
    result = ''
    while 1:
        N *= 2
        if N == 1.0:
            result += '1'
            break
        if N >= 1:
            result += '1'
            N -= 1
        else:
            result += '0'
        if len(result) >= 13:
            result = 'overflow'
            break

    print(f'#{tc}', end=' ')
    print(result)