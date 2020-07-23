"""
Single Number III
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:
Input:  [1,2,1,3,2,5]
Output: [3,5]

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitmask = 0
        for n in nums:
            bitmask ^= n
            
        diff = bitmask & (-bitmask)
        
        x = 0
        for n in nums:
            if n & diff:
                x ^= n

        return [x, bitmask^x]
