#Problem Statement: Given an integer array nums of length n, you want to create an array
#ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i]
#for 0 <= i < n (0-indexed).

def getConcatenation(nums):
        n = len(nums)
        ans = [0] * 2 * n
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans

nums = [1,3,2,1]
print(getConcatenation(nums))