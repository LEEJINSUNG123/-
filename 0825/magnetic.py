import sys; sys.stdin = open('magnetic.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc}')
    for i in range(N):
        print(arr[i])