def counting_sort(A, k):
    B = [0] * len(A)
    C = [0] * (k+1)

    for i in range(0, len(A)):
        C[A[i]] += 1

    for i in range(1, k+1):
        C[i] = C[i] + C[i - 1]

    for i in range(len(A)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
    return B


A = [4, 1, 3, 4, 3]

print(counting_sort(A, 4))
