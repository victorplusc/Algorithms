"""
78. Subsets
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
        return self.recursive(nums)
        return self.backtracking(nums)
    
    def recursive(self, nums):
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [curr + [num] for curr in output]
        return output
    

    def backtracking(self, nums):
        output = []
        n = len(nums)
        for k in range(n+1):
            self.bt_helper(nums, k, output, 0, [])
        return output
    
    def bt_helper(self, nums, k, output, first, curr):
        if len(curr) == k:
            output.append(curr[:])
        else:
            for i in range(first, len(nums)):
                curr.append(nums[i])
                self.bt_helper(nums, k, output, i+1, curr)
                curr.pop()
