"""
Subsets
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
# Time complexity: O(N*2**N)
# Space complexity: O(2**N)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(k, first, curr):
            if len(curr) == k:
                output.append(curr[:])
                return
            for i in range(first, n):
                curr.append(nums[i])
                backtrack(k, i+1, curr)
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n+1):
            backtrack(k, 0, [])
        return output
