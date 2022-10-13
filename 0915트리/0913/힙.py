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

# 최소힙
hsize = 0                   # 노드가 하나도 없는 상태(heap의 원소의 개수)
arr = [7, 2, 5, 3, 4, 6]       # 입력 정점
N = len(arr)
H = [0 for _ in range(N+1)]  # 이진 힙 구현을 위한 리스트 생성(크게 잡아야 함)

for i in range(N) : # 힙에 저장
    enq(arr[i])
print(H)
# for i in range(N) : # 출력 확인
#     print(deq(), end=' ')
# print()