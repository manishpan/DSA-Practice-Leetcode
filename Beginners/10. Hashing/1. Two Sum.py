#Problem statement: Given an array of integers nums and an integer target, return indices of the two numbers such 
#that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

def twoSums(nums, target):
    hashMap = dict()  #val : index

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hashMap:
            return [hashMap[diff], i]
        hashMap[nums[i]] = i

nums = [27,11,15]
target = 4
print(twoSums(nums, target))