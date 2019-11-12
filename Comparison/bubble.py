

def bubbleSort(A):
    n = len(A)
    for i in range(n):
        for j in range(n-i-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]