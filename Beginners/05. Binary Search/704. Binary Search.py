#Problem statement: Given an array of integers nums which is sorted in ascending order, and an integer target,
#write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

#You must write an algorithm with O(log n) runtime complexity.

def BinarySearch(nums, target):
    low, high = 0, len(nums)-1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target: high = mid - 1
        elif nums[mid] < target: low = mid + 1
        else:                    return mid

    return -1

nums = [-1, 0, 3, 5, 9, 12]
target = 2
print(BinarySearch(nums, target))