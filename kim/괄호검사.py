import sys; sys.stdin = open("괄호검사.txt")

def solve(str1):
    stack = []
    for i in range(len(str1)):
        if str1[i] == '(' or str1[i] == '{':
            stack.append(str1[i])
        elif str1[i] == ')' or str1[i] == '}':
            if len(stack) == 0:
                return 0
            else:
                tmp = stack.pop()
            # 비교
            if str1[i] == ')' and tmp != '(':
                return 0
            elif str1[i] == '}' and tmp != '{':
                return 0
    # 스택이 비어있는 지 확인
    if stack :
        return 0
    return 1

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    print(f'#{tc} {solve(str1)}')