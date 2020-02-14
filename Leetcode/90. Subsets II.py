"""
90. Subsets II
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
# Time complexity: O(2**N)
# Space complexity: O(2**N)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # return self.iterative(nums)
        return self.backtracking(nums)
        
    def iterative(self, nums):
        n = len(nums)
        output = [[]]
        start = size = 0
        for i in range(n):
            start = size if i >= 1 and nums[i] == nums[i-1] else 0
            size = len(output)
            for j in range(start, size):
                output.append(output[j] + [nums[i]])
        return output
    
    def backtracking(self, nums):
        output = []
        self.bt_helper(nums, 0, output, [])
        return output
    
    def bt_helper(self, nums, first, output, curr):
        output.append(curr[:])
        for i in range(first, len(nums)):
            if i == first or nums[i] != nums[i-1]:
                curr.append(nums[i])
                self.bt_helper(nums, i+1, output, curr)
                curr.pop()
