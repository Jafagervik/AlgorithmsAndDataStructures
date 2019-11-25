
def insertionSort(A):
    n = len(A)

    # Takes one card out at a time
    for i in range(1, n):
        #Goes through already sorted cards and places ours where it should be
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
