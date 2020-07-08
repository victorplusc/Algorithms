"""
311. Sparse Matrix Multiplication
Given two sparse matrices A and B, return the result of AB.
You may assume that A's column number is equal to B's row number.

Example:
Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:
     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |

Constraints:
1 <= A.length, B.length <= 100
1 <= A[i].length, B[i].length <= 100
-100 <= A[i][j], B[i][j] <= 100
"""
# Time complexity: O(A*B)
# Space complexity: O(A*B)
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        n_A, m_A = len(A), len(A[0])
        n_B, m_B = len(B), len(B[0])
        
        C = [[0] * m_B for _ in range(n_A)]
        
        for i in range(n_A):
            for j in range(m_A):
                if A[i][j] != 0:
                    for k in range(m_B):
                        if B[j][k] != 0:
                            C[i][k] += A[i][j] * B[j][k]
        return C
                        
