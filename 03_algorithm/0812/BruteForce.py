def brute_force(t, p):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j # 검색 시작 위치로...
            j = -1  # 처음으로 이동
        i = i + 1
        j = j + 1
    if j == M : return i - M
    else: return -1

def brute_force2(t, p):
    for i in range(N-M+1):
        flag = 1
        for j in range(M):
            if t[i+j] != p[j]:
                flag = 0
                break
        if flag:
            return i
    return -1

t = 'TTTTA'
p = 'TTA'
M = len(p)
N = len(t)
print(brute_force(t, p))
print(brute_force2(t, p))