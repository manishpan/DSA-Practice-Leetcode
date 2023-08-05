#problem statement: The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
#such that each number is the sum of the #two preceding ones, starting from 0 and 1

#Given n, calculate F(n)

def fib(n):
    f0, f1 = 0, 1
    res = n
    while n > 1:
        res = f0 + f1
        f0 = f1
        f1 = res
        n -= 1
    return res