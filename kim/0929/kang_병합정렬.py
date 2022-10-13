import sys; sys.stdin = open('병합정렬.txt')

def merge(left, right):
    # 두개의 left, right를 하나로 정렬하고 리턴
    result = []

    # 병합과정
    # 각각의 최소값(가장 왼쪽)을 비교해서 더 작은 요소를 결과에 추가
    # 왼쪽과 오른쪽에 요소가 없어질 때 까지
    while left or right:
        # left, right의 요소가 둘다 남아 있으면
        if left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        # 왼쪽만 남아있을 때
        elif left:
            result.append(left.pop(0))
        # 오른쪽만 남아 있을 때
        elif right:
            result.append(right.pop(0))

    return result


def merge_sort(m):
    global cnt
    # 문제를 절반으로 나누어서 각각을 해결하는 부분
    if len(m) == 1:
        return m
    # 안써도 되지만 구분하기 위해서 사용
    else:
        mid = len(m) // 2
        left = m[:mid]
        right = m[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        if left[-1] > right[-1]:
            cnt += 1

        return merge(left, right)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    ans = merge_sort(arr)
    print(f'#{t} {ans[N//2]} {cnt}')