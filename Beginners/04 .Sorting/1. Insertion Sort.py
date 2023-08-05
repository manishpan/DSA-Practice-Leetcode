def InsertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    print(arr)

def merge(arr, s, m, e):
    k = 0
    i, j = s, m+1
    l_arr, r_arr = [], []
    while i < m+1 and j < e+1:
        if arr[i] <= arr[j]:
            arr[k] = arr[i]
            i += 1
        else:
            arr[k] = arr[j]
            j += 1
        k += 1
    
    if i == m+1:
        while j < e+1:
            arr[k] = arr[j]
            j += 1
            k += 1
    elif j == e+1:
        while i < m+1:
            arr[k] = arr[i]
            i += 1
            k += 1

def mergeSort(arr, s, e):
    if e - s + 1 <= 1:
        return arr
    
    m = (e + s)/ 2
    mergeSort(arr, s, m)
    mergeSort(arr, m+1, e)

    merge(arr, s, m, e)

    return arr

def partition(arr):
    pivot = arr[-1]
    i, j = 0, 0
    for i in range(len(arr) - 1):
        if arr[i] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[j], arr[-1] = arr[-1], arr[i]

def BucketSort(arr):
    counts = [0] * (max(arr) + 1)
    n = len(arr)

    for i in range(n):
        counts[arr[i]] += 1

    i = 0
    for k in range(len(counts)):
        for j in range(counts[k]):
            arr[i] = k
            i += 1

arr = [6,2,4,1,3]
print(arr)
BucketSort(arr)
print(arr)