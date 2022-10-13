import sys; sys.stdin = open("쇠막대기.txt")

t = int(input())
for tc in range(1, 1+t):
    str1 = list(input())

    for i in range(len(str1)-1):
        if str1[i] == '(' and str1[i+1] == ')':
            str1[i] = '*'
            str1[i+1] = '^'
    print(str1)

    result = cnt = iron = 0

    for j in range(len(str1)-1):
        if str1[j] == '(':
            iron += 1
            cnt += 1
        elif iron > 0:
            if str1[j] == ')':
                iron -= 1
        if iron > 0 and str1[j] == '*':
            result += iron
    print(f'#{tc} {result+cnt}')