#Problem statement: Given an array nums with n objects colored red, white, or blue, sort them in-place so that
#objects of the same color are adjacent, with the colors in the order red, white, and blue.

#We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

#You must solve this problem without using the library's sort function.

def sortColors(nums) -> None:
    counts = [0, 0, 0]

    for i in range(len(nums)):
        counts[nums[i]] += 1

    i = 0
    for n in range(3):
        for j in range(counts[n]):
            nums[i] = n
            i += 1

nums = [2,0,2,1,1,0]
print(nums)
sortColors(nums)
print(nums)