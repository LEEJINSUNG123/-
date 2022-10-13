import sys; sys.stdin = open("특별한정렬.txt")

def selection_sort(a, n):
    for i in range(n-1):
        idx = i
        if i % 2:
            for j in range(i + 1, n):
                if a[idx] > a[j]:
                    idx = j
        else:
            for j in range(i + 1, n):
                if a[idx] < a[j]:
                    idx = j
        arr[i], arr[idx] = arr[idx], arr[i]

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    selection_sort(arr, n)
    print(arr[:10])