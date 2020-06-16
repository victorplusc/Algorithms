"""
368. Largest Divisible Subset
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:
Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)

Example 2:
Input: [1,2,4,8]
Output: [1,2,4,8]
"""
# Time complexity: O(N**2)
# Space complexity: O(N)
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        
        nums.sort()
        dp = [0] * len(nums)
        
        for i, num in enumerate(nums):
            max_subset_size = 0
            for k in range(0, i):
                if nums[i] % nums[k] == 0:
                    max_subset_size = max(max_subset_size, dp[k])
            max_subset_size += 1
            dp[i] = max_subset_size
        
        max_size, max_size_idx = max([(v, i) for i, v in enumerate(dp)])
        
        subset = []
        curr_size, curr = max_size, nums[max_size_idx]
        for i in range(max_size_idx, -1, -1):
            if curr_size == dp[i] and curr % nums[i] == 0:
                subset.append(nums[i])
                curr_size -= 1
                curr = nums[i]
        return subset
