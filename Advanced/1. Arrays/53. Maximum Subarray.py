#Problem Statement: Given an integer array nums, find the subarray with the largest sum, and return its sum.

#The solution to this problem is Kadane`s algorithm. We go through each element while maintaining a current sum, 
# and if current sum increases by adding an element we continue. If current sum becomes negative, we reset it to 0.
# For each element we maintain a maximum sum variable as well and update it when curSum > maxSum.`

class Solution:
    def maxSubArray(self, nums) -> int:
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            curSum = max(curSum, 0)     #If curSum is -ve, reset it to 0
            curSum += n
            maxSum = max(curSum, maxSum)
        
        return maxSum

#Testcases:
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))

nums = [1]
print(Solution().maxSubArray(nums))

nums = [5,4,-1,7,8]
print(Solution().maxSubArray(nums))