#Problem statement: You are given an m x n integer matrix matrix with the following two properties:

#Each row is sorted in non-decreasing order.
#The first integer of each row is greater than the last integer of the previous row.
#Given an integer target, return true if target is in matrix or false otherwise.

#You must write a solution in O(log(m * n)) time complexity.

def searchMatrix(matrix, target):
    row, column = len(matrix), len(matrix[0])
    
    top, bot = 0, row - 1
    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break
    
    if not (top <= bot):
        return False
    
    row = (top + bot) // 2
    low, high = 0, column - 1
    while low <= high:
        mid = (low + high) // 2
        if target < matrix[row][mid]:
            high = mid - 1
        elif target > matrix[row][mid]:
            low = mid + 1
        else:
            return True
    
    return False



matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 65
print(searchMatrix(matrix, target))