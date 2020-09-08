"""
33. Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""
# Time complexity: O(log N)
# Space complexity: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
