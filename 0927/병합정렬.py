import sys; sys.stdin = open('병합정렬.txt')



def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # for i in arr:
    #     if i < mid:
    #         L.append(i)
    #     else:
    #         R.append(i)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(right.popleft())
            else:
                result.append(left.popleft())
        elif len(left) > 0:
            for l in left:
                result.append(l)
        elif len(right) > 0:
            for r in right:
                result.append(r)
    return result

t = int(input())
for tc in range(1, t+1):
    print(f'#{tc} 0')
    N = int(input())
    arr = list(map(int, input().split()))
    print(merge_sort(arr))
