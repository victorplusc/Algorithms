"""
Number of Islands
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""

# Time complexity: O(N*M)
# Space complexity: O(N*M)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        n_islands = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    n_islands += 1
                    self.check_same_island(grid, y, x)
        return n_islands
    
    def check_same_island(self, grid, y, x):
        if y < 0 or x < 0 or y == len(grid) or x == len(grid[0]) or grid[y][x] != "1":
            return
        grid[y][x] = "X"
        self.check_same_island(grid, y+1, x)
        self.check_same_island(grid, y-1, x)
        self.check_same_island(grid, y, x+1)
        self.check_same_island(grid, y, x-1)
