import sys; sys.stdin = open('이진힙.txt')
import heapq

def enq(item):
    global hsize
    hsize += 1
    H[hsize] = item

    c = hsize
    p = hsize // 2

    while p and H[p] > H[c]:
        H[p], H[c] = H[c], H[p]
        c = p
        p = c // 2

t = int(input())
for tc in range(1, t+1):
    # N = int(input())
    # heap = list(map(int, input().split()))
    # heapq.heapify(heap)
    # heap = [0] + heap
    # sum = 0
    # while N > 0:
    #     N //= 2
    #     sum += heap[N]
    # print(f'#{tc} {sum}')
    hsize = 0
    N = int(input())
    arr = list(map(int, input().split()))
    H = [0 for _ in range(N+1)]
    for i in range(N):  # 힙에 저장
        enq(arr[i])
    total = 0
    while N > 0:
        N //= 2
        total += H[N]
    print(f'#{tc} {total}')