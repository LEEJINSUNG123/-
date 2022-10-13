import sys; sys.stdin = open('특별한정렬_input.txt')
def selection_sort(a, n):
    for i in range(10):
        idx = i
        if i % 2 == 0:
            # 최대값
            for j in range(i + 1, n):
                if a[idx] < a[j]:
                    idx = j
        else:
            # 최소값
            for j in range(i+1, n):
                if a[idx] > a[j]:
                    idx = j
        # 바꾸기
        arr[i], arr[idx] = arr[idx], arr[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    selection_sort(arr, N)

    print(f'#{tc}', end=' ')
    for i in range(10):
        print(arr[i], end=' ')
    print()


