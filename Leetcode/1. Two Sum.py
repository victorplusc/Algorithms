"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            d[num] = i
        
        for j, num in enumerate(nums):
            if target-num in d and j != d[target-num]:
                return sorted([d[target-num], j])
                
# Time complexity: O(N)
# Space complexity: O(N)
