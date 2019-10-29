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
        zeros = 0
        n = len(nums)
        curr = 0
        for i in nums:
            if i != 0:
                nums[curr] = i
                curr += 1
            else:
                zeros += 1
        for i in range(n-zeros, n):
            nums[i] = 0
