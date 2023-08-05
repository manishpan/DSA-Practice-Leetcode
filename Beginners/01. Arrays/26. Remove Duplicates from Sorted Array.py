#Problem statement: Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such
#that each unique element appears only once. The relative order of the elements should be kept the same.
#Then return the number of unique elements in nums.

def removeDuplicates(nums):
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j = j + 1
    return j

nums = [0,0,1,1,1,2,2,3,3,4]
k = removeDuplicates(nums)
print(k)
print(nums[:k])