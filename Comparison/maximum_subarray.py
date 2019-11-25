from math import inf

def Find_Max_SubArray(A, low, high):
    if low == high:
        return low, high, A[low]
    else:
        mid = (low+high)//2

        l_low, l_high, l_sum = Find_Max_Crossing_SubArray(A, low, mid)
        r_low, r_high, r_sum = Find_Max_Crossing_SubArray(A, mid, high)

        x_low, x_high, x_sum = Find_Max_Crossing_SubArray(A, low, mid, high)

        # Find best solution out of these three
        if l_sum > r_sum and l_sum > x_sum:
            return l_low, l_high, l_sum
        elif r_sum > l_sum and r_sum > x_sum:
            return r_low, r_high, r_sum
        else:
            return x_low, x_high, x_sum


def Find_Max_Crossing_SubArray(A, low, mid, high):

    l_sum = -inf
    sum = 0
    for i in range(mid, low, -1):
        sum += A[i]
        if sum > l_sum:
            l_sum = sum
            l_max = i

    r_sum = -inf
    sum = 0
    for j in range(mid, high+1):
        sum += A[j]
        if sum > r_sum:
            r_sum = sum
            r_max = j

    return l_max, r_max, l_sum + r_sum
