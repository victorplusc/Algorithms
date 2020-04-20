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
        return self.naive(nums, target)
        return self.modified_bin_search(nums, target)
        return self.inf_bin_search(nums, target)

    def naive(self, nums, target):
        n = len(nums)
        left, right = 0, n-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left
        left, right = 0, n-1
        while left <= right:
            mid = (left+right)//2
            actual_mid = (mid+pivot)%n
            if nums[actual_mid] == target:
                return actual_mid
            elif nums[actual_mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def modified_bin_search(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # nums[mid] < nums[left]
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
    
    def inf_bin_search(self, nums, target):
        left, right = 0, len(nums)-1
        
        while left < right:
            mid = (left+right)//2
            n = nums[mid]
            if (nums[mid] < nums[0]) != (target < nums[0]):
                n = -float('inf') if target < nums[0] else float('inf')
            if n < target:
                left = mid + 1
            elif n > target:
                right = mid
            else:
                return mid

        return -1
