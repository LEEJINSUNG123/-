import sys; sys.stdin = open('정식이.txt')
import copy

def two_ten(x):
    x = x[::-1]
    ans = 0
    for i in range(len(x)):
        ans += (2 ** i) * int(x[i])
    for j in three_l:
        if ans == j:
            return ans
    return 0

def three_ten(x):
    x = x[::-1]
    ans = 0
    for i in range(len(x)):
        ans += (3 ** i) * int(x[i])
    return ans

T = int(input())
for tc in range(1, T+1):
    two = list(input())
    three = list(input())
    three_l = []

    for j in range(len(three)):
        temp = copy.deepcopy(three)
        if three[j] == '0':
            temp[j] = '1'
            three_l.append(three_ten(temp))
            temp[j] = '2'
            three_l.append(three_ten(temp))
        elif three[j] == '1':
            temp[j] = '0'
            three_l.append(three_ten(temp))
            temp[j] = '2'
            three_l.append(three_ten(temp))
        elif three[j] == '2':
            temp[j] = '0'
            three_l.append(three_ten(temp))
            temp[j] = '1'
            three_l.append(three_ten(temp))

    result = 0
    for i in range(len(two)):
        temp = copy.deepcopy(two)
        if two[i] == '0':
            temp[i] = '1'
        else:
            temp[i] = '0'
        result = two_ten(temp)
        if result:
            print(f'#{tc} {result}')
            break


