import sys; sys.stdin = open('화물토크.txt')

# khw
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    jobs = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    # 종료시간기준으로 sort
    jobs.sort(key=lambda x:(x[1], x[0]))
    # print(jobs)
    finish = 0

    for i in range(N):
        if finish <= jobs[i][0]:
            ans += 1
            finish = jobs[i][1]
    print(f'#{tc} {ans}')





# t = int(input())
# for tc in range(1, t+1):
#     N = int(input())
#     arr = []
#     for _ in range(N):
#         s, e = map(int, input().split())
#         arr += [(e, s)]
#     arr.sort(reverse=True)
#     print(arr)
#     a = [0] * 24
#     cnt = len(arr)
#     for i in range(N-1):
#         if arr[i][1] == arr[i+1][0]:
#             pass
#         elif arr[i][1] > arr[i+1][0]:
#             pass
#         elif arr[i][1] < arr[i+1][0]:
#             cnt -= 1
#     print(cnt)