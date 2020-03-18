"""
137. Single Number II
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,3,2]
Output: 3

Example 2:
Input: [0,1,0,1,0,1,99]
Output: 99
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.hashmap(nums)
        return self.bitwise_op(nums)
    
    # Time complexity: O(N)
    # Space complexity: O(N)
    def hashmap(self, nums):
        counter = collections.Counter(nums)
        for k, v in counter.items():
            if v == 1:
                return k
        return 0
    
    # Time complexity: O(N)
    # Space complexity: O(1)
    def bitwise_op(self, nums):
        seen_once = seen_twice = 0
        
        for n in nums:
            seen_once = ~seen_twice & (seen_once^n)
            seen_twice = ~seen_once & (seen_twice^n)
        return seen_once
