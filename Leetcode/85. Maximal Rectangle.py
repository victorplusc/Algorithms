"""
85. Maximal Rectangle
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""
# Time complexity: O(N*M)
# Space complexity: O(M)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        n, m = len(matrix), len(matrix[0])
        left = [0] * m
        right = [m-1] * m
        height = [0] * m

        max_area = 0
        for y in range(n):
            curr_right = m-1
            for x in reversed(range(m)):
                if matrix[y][x] == "1": 
                    right[x] = min(right[x], curr_right)
                else:
                    right[x] = m-1
                    curr_right = x-1
            
            curr_left = 0
            for x in range(m):
                if matrix[y][x] == "1":
                    left[x] = max(left[x], curr_left)
                    height[x] += 1
                else:
                    left[x] = 0
                    height[x] = 0
                    curr_left = x+1
            
            for x in range(m):
                max_area = max(max_area, (right[x]-left[x]+1)*height[x])
                
        return max_area
