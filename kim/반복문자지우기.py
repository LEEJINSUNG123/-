import sys; sys.stdin = open("반복문자지우기.txt")

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    stack = []

    for i in range(len(str1)):
        if len(stack) == 0:
            stack.append(str1[i])
        else:
            if stack[-1] == str1[i]:
                stack.pop()
            else:
                stack.append(str1[i])
    print(f'#{tc} {len(stack)}')