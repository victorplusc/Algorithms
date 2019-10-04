"""
73. Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

# Time complexity: O(N*M)
# Space complexity: O(1)
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        left_col = False
        for y in range(rows):
            if matrix[y][0] == 0: 
                left_col = True
                
            for x in range(1, cols):
                if matrix[y][x] == 0:
                    matrix[y][0] = 0
                    matrix[0][x] = 0
        
        for y in range(1, rows):
            for x in range(1, cols):
                if matrix[y][0] == 0 or matrix[0][x] == 0:
                    matrix[y][x] = 0
        
        if matrix[0][0] == 0:
            for x in range(cols):
                matrix[0][x] = 0
        
        if left_col:
            for y in range(rows):
                matrix[y][0] = 0
