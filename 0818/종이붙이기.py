# dp
import sys; sys.stdin = open("종이붙이기.txt")

def paper(n):
    f = [1, 1]

    for i in range(2, n + 1):
        f.append(f[i-1] + 2 * f[i-2])
    return f[n]

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    n //= 10
    print(f'#{tc} {paper(n)}')