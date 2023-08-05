#Problem Statement: Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
#Return the array in the form [x1,y1,x2,y2,...,xn,yn].

def shuffle(nums, n):
        l = []
        for i in range(n):
            l.append(nums[i])
            l.append(nums[i + n])
        return l

nums = [1,1,2,2]
n = 2
shuffle(nums, n)
print(nums)