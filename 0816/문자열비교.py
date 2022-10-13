import sys; sys.stdin = open("문자열비교.txt", "r")

t = int(input())
for tc in range(1, t+1):
    str1 = input()
    str2 = input()
    flag = 0

    for i in range(len(str2)):
        if str2[i] == str1[0]:
            if str2[i:i+len(str1)] == str1:
                flag = 1
                break
    if flag:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')


