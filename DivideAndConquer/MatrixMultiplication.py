from math import *


def Multiplication(A, B, n):
    C = [[0 in range(n)] in range(n)]
    if n == 1:
        C[0][0] = A[0][0] * B[0][0]
    else:   # partition A, B, and C into n/2 * n/2 submatrices
        C[0][0] = Multiplication(A[0][0], B[0][0], n/2) + Multiplication(A[0][1], B[1][0], n/2)
        C[0][1] = Multiplication(A[0][0], B[1][0], n/2) + Multiplication(A[0][1], B[1][1], n/2)
        C[1][0] = Multiplication(A[1][0], B[0][1], n/2) + Multiplication(A[1][1], B[1][1], n/2)
        C[1][1] = Multiplication(A[1][0], B[0][1], n/2) + Multiplication(A[1][1], B[1][1], n/2)

    return C