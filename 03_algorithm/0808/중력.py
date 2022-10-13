import sys
sys.stdin = open('중력_input.txt')

T = int(input())  # 테스트케이스 갯수
for tc in range(1, T+1):
    N = int(input()) # 아래배열의 갯수
    arr = list(map(int, input().split()))
    # print(arr)

    result = 0  # 최대 낙차값
    for i in range(N):
        max_height = N - 1 - i  # i의 최대낙차값
        for j in range(i+1, N):
            if arr[i] <= arr[j]:
                max_height -= 1
        # 최대낙차값을 구하기
        if result < max_height:
            result = max_height

    print(f'#{tc} {result}')
