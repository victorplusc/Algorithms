"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        counts = [0 for i in range(len(nums))]
        
        for i in nums:
            counts[i-1] += 1
        
        return [i+1 for i in range(len(counts)) if counts[i]==0]
