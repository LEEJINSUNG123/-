import sys; sys.stdin = open("괄호검사.txt")

t = int(input())

for tc in range(1, t+1):
    str1 = input()
    stack = []
    flag = 1
    for i in range(len(str1)):
        if str1[i] == '{' or str1[i] == '(':
            stack.append(str1[i])
        elif str1[i] == '}' or str1[i] == ')':
            if len(stack) > 0:
                a = stack.pop()
                if a == '{' and str1[i] == ')':
                    flag = 0
                if a == '(' and str1[i] == '}':
                    flag = 0
            else:
                flag = 0
    if flag and len(stack) == 0:
        print(f'#{tc} {flag}')
    elif len(stack) != 0:
        print(f'#{tc} 0')
    elif flag == 0:
        print(f'#{tc} {flag}')

