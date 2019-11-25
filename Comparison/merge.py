from math import floor


def mergeSort(A):
    n = len(A)
    if n > 1:
        mid = n//2
        L = A[:mid]
        R = A[mid]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1


# Alternative method to implementing mergesort using two functions: MergeSort and Merge


def MergeSort(A, l, r):
    if l < r:
        mid = l + (l+r)//2

        MergeSort(A, l, mid)
        MergeSort(A, mid+1, r)

        Merge(A, l, mid, r)


def Merge(A, l, mid, r):

    n1 = mid - l + 1  # Size of first half
    n2 = r - mid      # Size of second half

    L = [0 for i in range(n1)]
    R = [0 for i in range(n2)]

    for i in range(n1):
        L[i] = A[l + i - 1]
    for j in range(n2):
        R[j] = A[mid + j]

    i = 1; j = 1
    for k in range(l, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

    #size of first, size of second, initialize empty array for both, set their values correctly, sort with i = 1; j = 1
