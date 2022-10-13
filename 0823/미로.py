import sys; sys.stdin = open("미로.txt")

# def backtracking():


t = int(input())
for tc in range(1, t+1):
    N = int(input())
    arr = [list(map(int, input())) for _  in range(N)]
    # print(arr)
    start_x = N - 1
    start_y = 0
    end_y = 0
    end_x = 0
    flag = 1
    for i in range(N):
        if arr[start_x][i] == 2:
            start_y = i
        else:
            flag = 0
        if arr[0][i] == 3:
            end_y = i
        else:
            flag = 0
    print(start_x, start_y)
    print(end_x, end_y)

