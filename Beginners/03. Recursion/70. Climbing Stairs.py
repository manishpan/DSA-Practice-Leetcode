#Problem statement: You are climbing a staircase. It takes n steps to reach the top.

#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climbStairs(n):
    f0, f1 = 1, 2
    res = n
    while n > 1:
        res = f0 + f1
        f0 = f1
        f1 = res
        n -= 1
    return res