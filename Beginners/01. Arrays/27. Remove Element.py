#Problem statment: Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
#The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

def removeElement(nums, val):
        i, j = 0, len(nums) - 1
        while i <= j:
            while j > -1 and nums[j] == val:
                j = j - 1
            if i < j and nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
            i = i + 1
        return j + 1

nums = [0,1,2,2,3,0,4,2]
val = 2
k = removeElement(nums, val)
print(k)
print(nums[:k])