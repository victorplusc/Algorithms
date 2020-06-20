"""
77. Combinations
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
# Time complexity: O(K*C(N, K))
# Space complexity: O(C(N, K))
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, curr=[]):
            if len(curr) == k:
                output.append(curr[:])
            for i in range(start, n+1):
                curr.append(i)
                backtrack(i+1, curr)
                curr.pop()
        output = []
        backtrack(1)
        return output
        
        
