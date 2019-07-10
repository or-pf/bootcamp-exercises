def power(x, n):
    if n == 0:
        ans = 1
    else:
        ans = x * power(x, n-1)
    return ans

power(2,3)