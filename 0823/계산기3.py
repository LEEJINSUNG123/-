import sys; sys.stdin = open("계산기.txt")

for tc in range(1, 11):
    SIZE = int(input())
    S = input()
    stack_infix = []
    stack_postfix = []

    for s in S:
        if s == '+':    # 1
            if (len(stack_infix) > 0 and stack_infix[-1] == '+') or (len(stack_infix) > 0 and stack_infix[-1] == '*'):
                for _ in range(len(stack_infix)):
                    if stack_infix[-1] == '+':
                        stack_postfix.append(stack_infix.pop())
                    elif stack_infix[-1] == '*':
                        stack_postfix.append(stack_infix.pop())
                stack_infix.append(s)
            else:
                stack_infix.append(s)

        elif s == '*':  # 2
            if len(stack_infix) > 0 and stack_infix[-1] == '*':
                stack_postfix.append(stack_infix.pop())
                stack_infix.append(s)
            else:
                stack_infix.append(s)

        elif s == '(':  # 3
            stack_infix.append(s)

        elif s == ')':
            if len(stack_infix) > 0:
                while stack_infix[-1] != '(' and len(stack_infix) > 0:
                    stack_postfix.append(stack_infix.pop())

                stack_infix.pop()
        else:
            stack_postfix.append(int(s))

    if len(stack_infix) > 0:
        for _ in range(len(stack_infix)):
            stack_postfix.append(stack_infix.pop())

    stack = []
    for i in range(len(stack_postfix)):
        if stack_postfix[i] == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif stack_postfix[i] == '*':
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        else:
            stack.append(stack_postfix[i])

    print(f'#{tc} {stack.pop()}')