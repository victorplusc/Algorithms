"""
Subarray Sum Equals K
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0: 1}
        res = 0
        curr = 0
        for n in nums:
            curr += n
            res += count.get(curr-k, 0)
            count[curr] = count.get(curr, 0) + 1
        return res
