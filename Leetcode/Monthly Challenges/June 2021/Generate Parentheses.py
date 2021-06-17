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
# Time complexity: exponential
# Space complexity: exponential
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        perms = []
        def backtrack(curr = [], left=0, right=0):
            if left+right == 2*n:
                perms.append("".join(curr))
                return
            if left < n:
                curr.append("(")
                backtrack(curr, left+1, right)
                curr.pop()
            if right < left:
                curr.append(")")
                backtrack(curr, left, right+1)
                curr.pop()
                
        backtrack()
        return perms
