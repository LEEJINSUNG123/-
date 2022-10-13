# 최소힙만 지원
import heapq
heap = [7, 2, 5, 3, 4, 6]
heapq.heapify(heap)
heap = [0] + heap
print(heap)
n = 6
sum = 0
while n > 0:
    n //= 2
    sum += heap[n]
print(sum)
print(heap[3])
# heapq.heappush(heap, 1)
# print(heap)
# while heap:
#     print(heapq.heappop(heap), end=' ')

# 최대힙 구현
# temp = [7, 2, 5, 3, 4, 6]
# heap2 = []
# for i in range(len(temp)):
#     heapq.heappush(heap2, -temp[i])
# print(heap2)
# while heap2:
#     print(heapq.heappop(heap2) * -1, end=' ')