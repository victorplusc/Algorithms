"""
695. Max Area of Island
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""
# Time complexity: O(N*M)
# Space complexity: O(N*M)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0       
        n, m = len(grid), len(grid[0])
        def dfs_island(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[y][x] != 1:
                return 0
            grid[y][x] = "X"
            return 1 + dfs_island(x-1, y) + dfs_island(x+1, y) + dfs_island(x, y-1) + dfs_island(x, y+1) 
        
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == 1:
                    area = dfs_island(x, y)
                    max_area = max(max_area, area)
                    
        return max_area
