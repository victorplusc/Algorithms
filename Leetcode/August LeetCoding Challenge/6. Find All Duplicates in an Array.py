"""
Find All Duplicates in an Array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
"""
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        
        for n in nums:
            if nums[abs(n)-1] < 0:
                duplicates.append(abs(n))
            nums[abs(n)-1] *= -1
        return duplicates
