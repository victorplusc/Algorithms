"""
463. Island Perimeter
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:
"""
# Time complexity: O(N+M)
# Space complexity: O(1)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        perimeter = 0
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == 1:
                    perimeter += self.surrounding_perimeter(grid, x, y, m, n)
        return perimeter
                
        
    def surrounding_perimeter(self, grid, x, y, m, n):
        perimeter = 4
        if x != 0 and grid[y][x-1] == 1:
            perimeter -= 2
        if y != 0 and grid[y-1][x] == 1:
            perimeter -= 2
        return perimeter
