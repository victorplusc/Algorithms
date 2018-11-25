#41. First Missing Positive
"""
Given an unsorted integer array, find the smallest missing positive integer.

1 is considered the lowest positive integer.
"""

class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = {i for i in nums if i >= 1}
        
        for i in range(1, len(numSet)+2):
            if i not in numSet: return i
