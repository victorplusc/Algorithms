#162. Find Peak Element
"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(nums)-1
        
        while left < right:
            mid = (left + right)//2
            if nums[mid] <= nums[mid+1]:
                left = mid+1
            else:
                right = mid
            
        return left
