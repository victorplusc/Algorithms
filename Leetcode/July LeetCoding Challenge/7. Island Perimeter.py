"""
Island Perimeter
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
        n = len(grid)
        if not n: return 0
        m = len(grid[0])
        
        perimeter = 0
        for y in range(n):
            for x in range(m):
                if grid[y][x] == 1:
                    perimeter += self.surrounding_perimeter(grid, y, x, n, m)
        return perimeter
    
    def surrounding_perimeter(self, grid, y, x, n, m):
        perimeter = 4
        if x > 0 and grid[y][x-1] == 1:
            perimeter -= 1
        if x < m-1 and grid[y][x+1] == 1:
            perimeter -= 1
        if y > 0 and grid[y-1][x] == 1:
            perimeter -= 1
        if y < n-1 and grid[y+1][x] == 1:
            perimeter -= 1
        return perimeter
