def my_strrev(s):
    # 문자열 S를 리스트로 변환
    arr = list(s)
    # for문을 이용해서 뒤집기
    for i in range(len(arr) // 2):
        arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
    # 리스트를 문자열로 변환
    s = ''.join(arr)

    return s

s = 'algorithm'
# s = my_strrev(s)
# s = s[::-1]
arr = list(s)
arr.reverse()
s = ''.join(arr)

print(s)
