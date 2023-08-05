#Problem Statement: Given an array of integers nums, sort the array in ascending order and return it.

def InsertionSort(nums):
    for i in range(1, len(nums)):
        j = i - 1
        key = nums[i]
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key

def QuickSort(nums, s, e):
    if e - s + 1 <= 1:
        return nums
    
    pivot = nums[e]
    i = s
    j = s
    while i < e:
        if nums[i] < pivot:
           nums[j], nums[i] = nums[i], nums[j]
           j += 1
        i += 1
    nums[j], nums[i] = nums[i], nums[j]

    QuickSort(nums, s, j-1)
    QuickSort(nums, j+1, e)

def Merge(nums, p, q, r):
    left, right = nums[p: q+1], nums[q+1:r+1]
    i, j = 0, 0
    k = p

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1
            
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

def MergeSort(nums, p, r):
    if r - p + 1 <= 1:
        return nums
            
    q = (p+r)//2
    MergeSort(nums, p, q)
    MergeSort(nums, q+1, r)
    Merge(nums, p, q, r)
        


nums = [5,2,0,3,1]
#InsertionSort(nums)
print(nums)
#QuickSort(nums, 0, len(nums)-1)
print(nums)
MergeSort(nums, 0, len(nums)-1)
print(nums)