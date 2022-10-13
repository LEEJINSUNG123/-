import sys; sys.stdin = open('세제곱근.txt')

def binary_search():
    low = 1
    high = N
    while low <= high:
        mid = (low + high) // 2
        key = mid ** 3
        if key == N:
            return mid
        elif key > N:
            high = mid - 1
        else:
            low = mid + 1
    # 세제곱근이 없을 때
    return -1

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    print(f'#{tc} {binary_search()}')