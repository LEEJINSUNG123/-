import sys; sys.stdin = open("이진탐색.txt")

def binary_search(arr, key, page):
    start = 1
    end = page
    cnt = 0
    while start <= end:
        cnt += 1
        middle = (start + end) // 2
        if key == arr[middle]:
            return cnt
        elif key < arr[middle]:
            end = middle
        else:
            start = middle
    # return -1

t = int(input())

for tc in range(1, t+1):
    P, A, B = map(int, input().split())
    arr = [0] + list(range(1, P+1))

    a = binary_search(arr, A, P)
    b = binary_search(arr, B, P)

    ans = '0'
    if a > b:
        ans = 'B'
    elif a < b:
        ans = 'A'
    print(f'#{tc} {ans}')

'''
t = int(input())

for tc in range(1, t+1):
    p, pa, pb = list(map(int, input().split()))
    ca = cb = int((1+p)/2)
    # cnt_a = cnt_b = 0
    paa = p
    pbb = p
    starta = startb = 1

    while 1:
        if ca > pa:
            paa = ca
            ca = int((starta+paa)/2)
            # cnt_a += 1
        elif ca < pa:
            starta = ca
            ca = int((starta+paa)/2)
            # cnt_a += 1
        if cb > pb:
            pbb = cb
            cb = int((startb + pbb) / 2)
            # cnt_b += 1
        elif cb < pb:
            startb = cb
            cb = int((startb + pbb) / 2)
            # cnt_b += 1
        if ca == pa and cb == pb:
            print(f'#{tc} 0')
            break
        elif ca == pa:
            print(f'#{tc} A')
            break
        elif cb == pb:
            print(f'#{tc} B')
            break
'''