"""
40. Combination Sum II
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""
# Time complexity: O(2**N)
# Space complexity: O(2**N)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(idx, curr, remainder):
            if remainder == 0:
                output.append(curr[:])
                return
            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if remainder < candidates[i]:
                    break
                curr.append(candidates[i])
                backtrack(i+1, curr, remainder-candidates[i])
                curr.pop()
        
        counter = collections.Counter(candidates)
        candidates.sort()
        n = len(candidates)
        output = []
        backtrack(0, [], target)
        return output
