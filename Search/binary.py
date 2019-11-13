
def Binary_Search(A, target, L, R):
    """
    Complexity O(Log(n))
    :param A: List<Int>, Sorted list of integers
    :param target: Int, Value to find in list
    :param L: Int, Leftmost index
    :param R: Int, Rightmost index
    :return:
    """
    while L <= R:
        mid = L + (R - L) // 2
        if A[mid] == target:
            return mid
        if A[mid] < target:
            Binary_Search(A, target, L, mid -1)
        else:
            Binary_Search(A, target, mid + 1, R)
    return -1
