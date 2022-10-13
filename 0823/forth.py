import sys; sys.stdin = open("forth.txt")

T = int(input())
for tc in range(1, T+1):
    arr = list(map(str, input().split()))
    stack = []

    cnt = cnt2 = 0
    for j in range(len(arr)):
        if arr[j] == '+' or arr[j] == '-' or arr[j] == '*' or arr[j] == '/':
            cnt2 += 1
        elif arr[j] == '.':
            pass
        else:
            cnt += 1

    if cnt == (cnt2 + 1):
        for i in range(len(arr)):
            if arr[i] == '+':
                if len(stack) >= 2:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a + b)
                else:
                    print(f'#{tc} error')
                    break
            elif arr[i] == '-':
                if len(stack) >= 2:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a - b)
                else:
                    print(f'#{tc} error')
                    break
            elif arr[i] == '*':
                if len(stack) >= 2:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a * b)
            elif arr[i] == '/':
                if len(stack) >= 2:
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a / b)
            elif i == (len(arr)-1) and arr[i] == '.':
                if len(stack) == 1:
                    print(f'#{tc} {stack.pop()}')
                else:
                    print(f'#{tc} error')
                    break
            else:
                if arr[i] == '.':
                    print(f'#{tc} error')
                    break
                else:
                    stack.append(int(arr[i]))
    else:
        print(f'#{tc} error')