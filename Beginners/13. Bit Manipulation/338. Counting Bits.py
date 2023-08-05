#Problem Statement: Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
#ans[i] is the number of 1's in the binary representation of i.

def countBits(n):
    ans = []
    for i in range(0, n+1):
        res = 0
        while i:
            i = i & (i-1)
            res += 1
        ans.append(res)
    return ans

print(countBits(5))