"""
540. Single Element in a Sorted Array
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
 
Note: Your solution should run in O(log n) time and O(1) space.
"""
# Time complexity: O(logN)
# Space complexity: O(1)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums)
        while left < right:
            mid = (left+right)//2
            if (mid == len(nums)-1 and nums[mid] != nums[mid-1]) or nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
                return nums[mid]
            if mid%2 == 0:
                if nums[mid+1] != nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid-1] != nums[mid]:
                    right = mid
                else:
                    left = mid + 1
        return -1
