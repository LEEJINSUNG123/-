def itoa(num):
    arr = []
    while num:
        arr.append(num % 10)
        num //= 10
    return arr[::-1]

num = 123
arr = itoa(num)
print(arr)
