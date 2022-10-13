import time
start_time = time.time()
import sys; sys.stdin = open('5204_병합정렬_input.txt')
from collections import deque

def merge(left, right):
    # 두개의 left, right를 하나로 정렬하고 리턴
    result = []
    left = deque(left)
    right = deque(right)
    # 병합과정
    # 각각의 최소값들(가장 왼쪽)을 비교해서 더 작은 요소를 결과에 추가
    # left, right에 요소가 없어질때 까지 반복
    while left and right:
        # left, right의 요소가 둘 다 남아 있으면
        if left[0] <= right[0]:
            result.append(left.popleft())
        else:
            result.append(right.popleft())

    # 왼쪽만 남아 있으면
    if left:
        # result.append(left.popleft())
        result.extend(left)
    # 오른쪽만 남아 있으면
    if right:
        # result.append(right.popleft())
        result.extend(right)
    return result

def merge_sort(a):
    global cnt
    # 문제를 절반으로 나누어서 각각을 해결하는 부분
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



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = merge_sort(arr)
    print(f'#{tc} {arr[N//2]} {cnt}')

print(time.time()-start_time, 'seconds')