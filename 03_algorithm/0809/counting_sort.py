def counting_sort(A, B, k):
    C = [0] * (k + 1)

    # 카운팅
    for i in range(len(A)):
        C[A[i]] += 1
    # 누적
    for i in range(1, len(C)):
        C[i] += C[i-1]
    # 자리찾기
    for i in range(len(B)-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]

a = [0, 4, 1, 3, 1, 2, 4, 1]
b = [0] * len(a)
counting_sort(a, b, 4)
print(b)
