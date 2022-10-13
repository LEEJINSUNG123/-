# 최소힙만 지원
import heapq
# heap = [7, 2, 5, 3, 4, 6]
# heapq.heapify(heap)
# print(heap)
# heapq.heappush(heap, 1)
# print(heap)
# while heap:
#     print(heapq.heappop(heap), end=' ')

# 최대힙 구현
temp = [7, 2, 5, 3, 4, 6]
heap2 = []
for i in range(len(temp)):
    heapq.heappush(heap2, -temp[i])
print(heap2)
while heap2:
    print(heapq.heappop(heap2) * -1, end=' ')