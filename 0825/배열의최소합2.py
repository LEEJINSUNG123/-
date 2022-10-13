import sys; sys.stdin = open("배열최소합.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 987654321

    A = []
    for i in range(N):
        for j in range(N):
            if i != j:
                for x in range(N):
                    if x != i and x != j:
                        A.append([i, j, x])
    print(A)
    sum_v = 0
    for x in range(N):
        print(arr[x][A[x][x]])
    # if min_v > sum_v:
    #     min_v = sum_v
    # print(min_v)