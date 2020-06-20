"""
283. Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_nonzero = 0
        for i, val in enumerate(nums):
            if val != 0:
                nums[last_nonzero] = val
                last_nonzero += 1
        for i in range(last_nonzero, len(nums)):
            nums[i] = 0
