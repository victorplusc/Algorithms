"""
377. Combination Sum IV
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:
nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # return self.backtracking(nums, target)
        return self.dp(nums, target)
    
    # Time complexity: O(2**N)
    # Space complexity: O(N)
    def dp(self, nums, target):
        dp = [0] * (target+1)
        dp[0] = 1
        for val in range(1, len(dp)):
            for j in range(len(nums)):
                if val - nums[j] >= 0:
                    dp[val] += dp[val - nums[j]]
        return dp[-1]
    
    # Time complexity: O(2**N)
    # Space complexity: O(2**N)
    def backtracking(self, nums, target):
        def backtrack(remainder):
            if remainder == 0: 
                return 1
            if remainder in memo: 
                return memo[remainder]
            if remainder < 0:
                return 0
            count = 0
            for i in range(n):
                count += backtrack(remainder-nums[i])
            memo[remainder] = count
            return count
    
        if not nums: return 0
        
        memo = {}
        n = len(nums)
        return backtrack(target)
