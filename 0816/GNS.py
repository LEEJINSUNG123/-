import sys; sys.stdin = open("GNS.txt", "r")

# digit = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV','SIZ', 'SVN', 'EGT', 'NIN']
# t = int(input())
# for tc in range(1, t+1):
#     a, b = input().split()
#     arr = list(map(str, input().split()))
#
#     count = [0] * 10
#     for item in arr:
#         for j in range(10):
#             if item == digit[j]:
#                 count[j] += 1
#
#     print(f'#{tc}')
#     for i in range(10):
#         for _ in range(count[i]):
#             print(digit[i], end = ' ')
#     print()

def gns(arr):
    for i in range(N - 1):
        min = i
        for j in range(i + 1, N):
            if num.index(arr[min]) > num.index(arr[j]):
                min = j
        arr[i], arr[min] = arr[min], arr[i]

    return ' '.join(arr)


T = int(input())
for tc in range(1, T + 1):
    num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    TC, N = map(int, input().lstrip('#').split())
    arr = list(input().split())
    print(f'#{TC}')
    print(gns(arr))