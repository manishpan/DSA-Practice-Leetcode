#Problem statement: Given an integer array nums and an integer k, return the kth largest element in the array.

#Note that it is the kth largest element in the sorted order, not the kth distinct element.

def findKthLargest(nums, k):
    new_k = len(nums) - k

    def quickSelect(s, e):
        pivot = nums[e]
        j = s
        for i in range(s, e):
            if nums[i] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        nums[e], nums[j] = nums[j], nums[e]

        if j < new_k: return quickSelect(j+1, e)
        elif j > new_k: return quickSelect(s, j-1)
        else:           return pivot

    return quickSelect(0, len(nums)-1)
    
nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums, k))
print(nums)