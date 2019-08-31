"""
200. Number of Islands
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""

# Time complexity: O(N*M)
# Space complexity: O(N*M)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        islands = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    self.dfs(grid, y, x)
                    islands += 1
        return islands
    
    def dfs(self, grid, y, x):
        if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]) or grid[y][x] != "1":
            return
        grid[y][x] = "X"
        self.dfs(grid, y+1, x)
        self.dfs(grid, y-1, x)
        self.dfs(grid, y, x+1)
        self.dfs(grid, y, x-1)
        
        
# ================================== FINDING MAXIMUM ISLAND SIZE (VARIANT) ==================================

# Time complexity: O(N*M)
# Space complexity: O(N*M)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        size = 0
        islands = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    size = max(self.dfs(grid, y, x), size)
                    islands += 1
        
        return islands
    
    def dfs(self, grid, y, x):
        if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]) or grid[y][x] != "1":
            return
        if grid[y][x] == "1":
            size = 1
        else:
            size = 0
        grid[y][x] = "X"
        y1_size = self.dfs(grid, y+1, x)
        y2_size = self.dfs(grid, y-1, x)
        x1_size = self.dfs(grid, y, x+1)
        x2_size = self.dfs(grid, y, x-1)
        
        if y1_size:
            size += y1_size
        if y2_size:
            size += y2_size
        if x1_size:
            size += x1_size
        if x2_size:
            size += x2_size
    
        return size
