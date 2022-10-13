import sys; sys.stdin = open("forth.txt")

T = int(input())
for tc in range(1, T+1):
    arr = list(map(str, input().split()))
    stack = []

    cnt = cnt2 = cnt3 = 0
    for j in range(len(arr)):
        if arr[j] == '+' or arr[j] == '-' or arr[j] == '*' or arr[j] == '/':
            cnt2 += 1
        elif arr[j] == '.':
            cnt3 += 1
        else:
            cnt += 1

    if cnt3 > 1:
        print(f'#{tc} error')
        break

    if cnt == (cnt2 + 1):
        for i in range(len(arr)):
            if arr[i] == '+' or arr[i] == '-' or arr[i] == '*' or arr[i] == '/':
                if len(stack) >= 2:
                    b = stack.pop()
                    a = stack.pop()
                    if arr[i] == '+':
                        stack.append(a + b)
                    elif arr[i] == '-':
                        stack.append(a - b)
                    elif arr[i] == '*':
                        stack.append(a * b)
                    elif arr[i] == '/':
                        stack.append(a // b)
                else:
                    print(f'#{tc} error')
                    break
            elif arr[i] == '.':
                x = stack.pop()
                if len(stack) >= 1:
                    print(f'#{tc} error')
                    break
                else:
                    print(f'#{tc} {x}')
                    break
            else:
                stack.append(int(arr[i]))
    else:
        print(f'#{tc} error')