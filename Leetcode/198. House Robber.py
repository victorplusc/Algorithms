"""
198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution:
    ## Bottom-up DP, more coherent
    # Time complexity: O(N)
    # Space complexity: O(1)
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        prev_max = 0
        curr_max = 0
        for val in nums:
            temp = curr_max
            curr_max = max(prev_max + val, curr_max)
            prev_max = temp
        return curr_max

## Bottom-up DP
# Time complexity: O(N)
# Space complexity: O(N)
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dp = [0, nums[0]]
        for i in range(1,len(nums)):
            val = nums[i]
            dp.append(max(dp[-1], dp[-2]+val))
        return dp[-1]
"""

## Top-down recursive
# Time complexity: O(N)
# Space complexity: O(N)
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.rob_helper(nums,len(nums)-1,{})
    
    def rob_helper(self, nums: List[int], i, memo: dict) -> int:
        if i<0:
            return 0
        if i in memo:
            return memo[i]
        res = max(self.rob_helper(nums,i-2,memo)+nums[i], self.rob_helper(nums,i-1,memo))
        memo[i] = res
        return res
"""
