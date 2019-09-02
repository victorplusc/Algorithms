"""
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

# Time and space complexity: just say O(2**n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.perms = []
        self.backtrack(n, [], 0, 0)
        return self.perms
    
    def backtrack(self, n, curr, left, right):
        if len(curr) == 2*n:
            self.perms.append("".join(curr))
            return
        if left < n:
            self.backtrack(n, [_ for _ in curr] + ["("], left + 1, right)
        if right < left:
            self.backtrack(n, [_ for _ in curr] + [")"], left, right + 1)
