

def Fibonacci(n):
    f = [0 for i in range(n+1)]
    f[0] = 0
    f[1] = 1
    if n <= 1:
        return f[n]
    else:
        for i in range(2, n):
            f[i] += (f[i - 2] + f[i - 1])

    return f[n]
