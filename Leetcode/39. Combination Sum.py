"""
39. Combination Sum
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
# Time complexity: O(k * 2**n)
# Space complexity: O(k * 2**n)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.dfs(candidates, target)
        return self.dp(candidates, target)

    def dfs(self, candidates, target):
        def backtrack(remainder, idx, curr):
            if remainder == 0:
                output.append(curr[:])
                return
            for i in range(idx, n):
                if candidates[i] > remainder:
                    break
                curr.append(candidates[i])
                backtrack(remainder-candidates[i], i, curr)
                curr.pop()
        n = len(candidates)
        candidates.sort()
        output = []
        backtrack(target, 0, [])
        return output

    def dp(self, candidates, target):
        candidates.sort()
        dp = []
        for i in range(1, target+1):
            curr = []
            for j in range(len(candidates)):
                if candidates[j] > i:
                    break
                if candidates[j] == i:
                    curr.append([candidates[j]])
                else:
                    if i-candidates[j]-1 >= 0:
                        curr.extend(perm + [candidates[j]] for perm in dp[i-candidates[j]-1] if candidates[j] >= perm[-1])
            dp.append(curr)
        return dp[-1]
