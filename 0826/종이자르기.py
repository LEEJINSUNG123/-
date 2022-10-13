import sys; sys.stdin = open('종이자르기.txt')

x, y = map(int, input().split())
arr = [[1] * x for _ in range(y)]
N = int(input())
for i in range(N):


print(arr)