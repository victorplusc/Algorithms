"""
34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
# Time complexity: O(log N)
# Space complexity: O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.search_leftmost_idx(nums, 0, len(nums)-1, target)
        
        if left == -1: return [-1, -1]
        
        right = self.search_rightmost_idx(nums, left, len(nums)-1, target)
        return [left, right]
        
    def search_leftmost_idx(self, nums, left, right, target):
        found = False
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                found = True
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left if found else -1
            
    def search_rightmost_idx(self, nums, left, right, target):
        while left <= right:
            mid = (left+right)//2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return left-1
            
