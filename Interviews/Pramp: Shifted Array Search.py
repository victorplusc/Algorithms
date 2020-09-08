"""
Shifted Array Search
A sorted array of distinct integers shiftArr is shifted to the left by an unknown offset and you don’t have a pre-shifted copy of it. For instance, the sequence 1, 2, 3, 4, 5 becomes 3, 4, 5, 1, 2, after shifting it twice to the left.

Given shiftArr and an integer num, implement a function shiftedArrSearch that finds and returns the index of num in shiftArr. If num isn’t in shiftArr, return -1. Assume that the offset can be any value between 0 and arr.length - 1.

Explain your solution and analyze its time and space complexities.

Example:
input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2 # shiftArr is the
                                                 # outcome of shifting
                                                 # [2, 4, 5, 9, 12, 17]
                                                 # three times to the left

output: 3 # since it’s the index of 2 in arr
"""
def shifted_arr_search(nums, target):
    n = len(nums)
    start, end = 0, n-1
    while start <= end:
        mid = (start+end)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[0]:
            if target >= nums[0] and target < nums[mid]:
                end = mid-1
            else: #target < nums[0] or target > nums[mid]
                start = mid+1
        else: #nums[mid] < nums[0]
            if target <= nums[-1] and target > nums[mid]:
                start = mid + 1
            else: #target > nums[-1] or target < nums[mid]
                end = mid - 1
    return -1
