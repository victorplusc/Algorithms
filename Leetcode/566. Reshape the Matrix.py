"""
566. Reshape the Matrix
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the row number and column number of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 100
-1000 <= mat[i][j] <= 1000
1 <= r, c <= 300
"""
# Time complexity: O(N*M)
# Space complexity: O(N*M)
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not mat or r*c != len(mat)*len(mat[0]):
            return mat
        if len(mat) == r and len(mat[0]) == c:
            return mat

        output = []
        row_to_add = []
        for y, row in enumerate(mat):
            for x, val in enumerate(row):
                row_to_add.append(val)
                if len(row_to_add) == c:
                    output.append(row_to_add)
                    row_to_add = []
        return output
    
    # Time complexity: O(N*M)
    # Space complexity: O(N*M), including result
    def using_math(self, nums, r, c):
        if not nums or r*c != len(nums[0])*len(nums):
            return nums
        
        reshaped = [[None for i in range(c)] for j in range(r)]
        count = 0
        
        for row in nums:
            for v in row:
                reshaped[count//c][count%c] = v
                count += 1
        return reshaped
