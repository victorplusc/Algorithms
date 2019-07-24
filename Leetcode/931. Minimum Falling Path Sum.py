"""
931. Minimum Falling Path Sum
Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.
"""
# Time complexity: O(N**2)
# Space complexity: O(1)
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        while len(A) >= 2:
            row = A.pop()
            for i in range(len(row)):
                A[-1][i] += min(row[max(0,i-1):min(len(row),i+2)])
        return min(A[0])
            
            
