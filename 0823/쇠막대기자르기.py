# import sys; sys.stdin = open('쇠막대기.txt')

T = int(input())
for tc in range(1, T+1):
    arr = input()
    cnt = 0
    stick = 0
    for i in range(len(arr)):
        if arr[i] == '(':   # 왼쪽괄호
            stick += 1
        else:
            stick -= 1
            if arr[i-1] == '(': # 레이저
                cnt += stick
            else:   # 레이저 아님
                cnt += 1
    print(f'#{tc} {cnt}')