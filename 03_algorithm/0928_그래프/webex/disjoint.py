def make_set(x):
    p[x] = x

def find_set(x):
    if p[x] == x:
        return x
    else:
        return find_set(p[x])

def union(x, y):
    # x의 대표자, y의 대표자
    p[find_set(y)] = find_set(x)


# 1 ~ 6 까지 정점
N = 7
p = [0] * (N+1)
for i in range(1, N+1):
    make_set(i)

print(p)
union(2, 3)
union(4, 5)
union(4, 6)
union(7, 4)
print(p)
print(find_set(3))
print(find_set(6))