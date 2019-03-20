def binarySearch(array, target):

    left = 0
    right = len(array)-1

    while left <= right:
        mid = (left+right)//2

        if array[mid] == target:
            return mid
        
        if array[mid] < target:
            left = mid + 1
            
        if array[mid] > target:
            right = mid - 1

    return -1
