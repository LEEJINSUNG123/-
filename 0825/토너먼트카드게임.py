import sys; sys.stdin = open('토너먼트카드게임.txt')

def game(left, right):
    if left == right:
        return left
    else:
        r1 = game(left, (left + right) // 2)
        r2 = game((left+right)//2 + 1 , right)
        return win(r1,r2)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    print(f'#{tc} {game(1, N)}')