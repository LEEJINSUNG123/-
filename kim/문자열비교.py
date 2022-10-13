import sys; sys.stdin = open("문자열비교.txt", "r")

def brute_force(pattern, text):
    for i in range(n-m+1):
        flag = 1
        for j in range(m):
            if text[i+j] != pattern[j]:
                flag = 0
                break
        if flag:
            return 1
    return 0


t = int(input())
for tc in range(1, t+1):
    pattern = input()
    text = input()
    n = len(text)
    m = len(pattern)

    # for i in range(len(str2)):
    #     if str2[i] == str1[0]:
    #         if str2[i:i+len(str1)] == str1:
    #             flag = 1
    #             break

    print(f'#{tc} {brute_force(pattern, text)}')