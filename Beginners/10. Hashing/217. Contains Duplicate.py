#Problem statement: Given an integer array nums, return true if any value appears at least twice in the array,
#and return false if every element is distinct.

def containsDuplicate(nums):
    hashSet = set()

    for i in nums:
        if i in hashSet:
            return True
        hashSet.add(i)
    return False

nums = [1,2,3,2]
print(containsDuplicate(nums)) 