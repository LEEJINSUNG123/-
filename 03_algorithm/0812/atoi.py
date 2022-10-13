def atoi(arr):
    value = 0
    for i in range(len(arr)):
        value = value * 10 + arr[i]
    return value

arr = [1, 2, 3]
num = atoi(arr)
print(num + 1)