"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = {num:i for i, num in enumerate(nums)}
        
        for i, num in enumerate(nums):
            if target - num in indices and i != indices[target-num]:
                return sorted([indices[target-num], i])
                
# Time complexity: O(N)
# Space complexity: O(N)
