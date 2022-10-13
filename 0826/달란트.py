'''
#1 36
#2 1024
#3 46656
#4 1679616
#5 26214400
#6 2448880128
#7 125524238436
#8 2821109907456
#9 162679413013056
#10 5856458868470016
'''
import sys; sys.stdin = open('달란트.txt')

T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())
    Q = N // P
    R = N % P
    arr = [Q] * (P-R) + [Q+1] * R
    result = 1
    for i in arr:
        result *= i
    print(f'#{tc} {result}')
