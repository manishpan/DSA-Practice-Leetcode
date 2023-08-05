def BinarySearch(arr, target):
    low, high = 0, len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:   low = mid + 1
        elif arr[mid] > target: high = mid - 1
        else:                   return mid
    
    return -1

arr = [1,3,3,4,5,6,7,8]
target = 3
print(BinarySearch(arr, target))