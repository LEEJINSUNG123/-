import sys; sys.stdin = open('병합정렬.txt')
from collections import deque

def merge(left, right):
    result = []
    left = deque(left)
    right = deque(right)
    # 병합과정
    # 각각의 최솟값을 비교해서 결과에 추가...
    # left, right에 요소가 없어질 때까지 반복
    while left and right:
        # left, right의 요소가 둘 다 남아 있으면
        if left[0] <= right[0]:
            result.append(left.popleft())
        else:
            result.append(right.popleft())
        # left만 남아 있으면
    if left:
        result.extend(left)
    # rifht만 남아 있으면
    if right:
        result.extend(right)

    return result


def merge_sort(a):
    global cnt
    if len(a) == 1:
        return a
    else:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        if left[-1] > right[-1]:
            cnt += 1

        return merge(left, right)

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    ans = merge_sort(arr)
    print(f'#{t} {ans[N//2]} {cnt}')