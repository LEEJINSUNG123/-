import sys; sys.stdin = open("반복문자지우기.txt")

def remove(str1):
    str2 = []
    cnt = 0
    for i in range(len(str1) - 1):
        if str1[i] == str1[i + 1]:
            str1[i] = ''
            str1[i + 1] = ''
        else:
            cnt += 1
    if cnt == len(str1)-1:
        return len(str1)
    for j in range(len(str1)):
        if str1[j] != '':
            str2.append(str1[j])
    return remove(str2)


t = int(input())
for tc in range(1, t+1):
    str1 = list(input())
    print(f'#{tc}', end=' ')
    print(remove(str1))