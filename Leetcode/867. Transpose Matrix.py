"""
867. Transpose Matrix

Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.
"""

# Time complexity: O(N*M), where N is the number of rows, and M is the length of the row
# Space comexplity: O(N*M)
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        x = len(A[0])
        y = len(A)
        
        tr = [[None for i in range(y)] for j in range(x)]
        for i in range(x):
            for j in range(y):
                tr[i][j] = A[j][i]
        
        return tr
