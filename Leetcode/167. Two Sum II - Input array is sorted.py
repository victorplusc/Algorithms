"""
167. Two Sum II - Input array is sorted
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
"""

# Time complexity: O(N)
# Space complexity: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        if len(numbers) < 2:
            return []
        
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            if target - numbers[left] < numbers[right]:
                right -= 1
            elif target - numbers[left] > numbers[right]:
                left += 1
            else:
                return [left+1, right+1]
            
