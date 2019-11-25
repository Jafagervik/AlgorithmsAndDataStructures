
def CountingSort(A, B, n, k):
    """

    :param A: List<Int>, INPUT: list of numbers to sort through
    :param B: List<Int>, Array for storing the sorted numbers in
    :param n: Int, number of elements to sort
    :param k: Int, span of numbers to sort (highest number - lowest number)
    :return: List<Int>, The sorted array B
    """
    C = [0 for i in range(k)]
    for j in range(1, k):
        C[A[j]] += 1

    #Cumulative addition in array C
    for i in range(1, k):
        C[i] += C[i - 1]

    #Set
    for j in range(n, 0, -1):
        B[C[A[j]]] = A[j]
        C[A[j]] -= 1

    return B
