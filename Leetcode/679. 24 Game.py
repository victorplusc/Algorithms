"""
679. 24 Game
You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24

Example 2:
Input: [1, 2, 1, 2]
Output: False

Note:
The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
"""
# Time complexity: O(1)
# Space complexity: O(1)
from operator import truediv, mul, add, sub
class Solution:
    def judgePoint24(self, A: List[int]) -> bool:
        if not A: return False
        
        n = len(A)
        if n == 1:
            return abs(A[0] - 24) < 1e-6
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    B = [A[k] for k in range(n) if i != k != j]
                    for op in (truediv, mul, add, sub):
                        if (op is add or op is mul) and i < j: 
                            continue
                        if op is not truediv or A[j]:
                            B.append(op(A[i], A[j]))
                            if self.judgePoint24(B): return True
                            B.pop()
        return False
