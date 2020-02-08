"""
300. Longest Increasing Subsequence
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # return self.naive_recursive(nums, -float('inf'), 0)
        return self.memoized(nums, -float('inf'), 0, collections.defaultdict(dict))
        
    # Time complexity: O(2**N)
    # Space complexity: O(N**2)
    def naive_recursive(self, nums, prev, curr):
        if curr == len(nums):
            return 0
        taken = 0
        if nums[curr] > prev:
            taken = 1 + self.naive_recursive(nums, nums[curr], curr+1)
        not_taken = self.naive_recursive(nums, prev, curr+1)
        return max(taken, not_taken)
    
    # Time complexity: O(N**2)
    # Space complexity: O(N**2)
    def memoized(self, nums, prev, curr, memo):
        if curr == len(nums):
            return 0
        if prev in memo and curr in memo:
            return memo[prev][curr]
        taken = 0
        if prev < 0 or nums[curr] > nums[prev]:
            taken = 1 + self.memoized(nums, curr, curr+1, memo)
        not_taken = self.memoized(nums, prev, curr+1, memo)
        memo[prev][curr] = max(taken, not_taken)
        return memo[prev][curr]
