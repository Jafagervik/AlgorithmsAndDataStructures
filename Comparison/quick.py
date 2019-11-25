
def quickSort(A, l, h):
    if l < h:

        pi = partition(A, l, h)

        quickSort(A, l, pi-1)
        quickSort(A, pi+1, h)


def partition(A, l, h):
    pivot = A[h]

    i = l - 1

    for j in range(l, h):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[h] = A[h], A[i+1]

    return i+1


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr,0,n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" %arr[i]),