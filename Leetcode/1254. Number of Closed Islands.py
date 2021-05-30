"""
1254. Number of Closed Islands
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

Example 1:
Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:
Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

Example 3:
Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2

Constraints:
1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
"""
# Time complexity: O(N*M)
# Space complexity: O(N*M)
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # 0s is land, 1s is water
        
        n, m = len(grid), len(grid[0])
        
        # idea: mark islands
        def convert_land(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[y][x] != 0:
                return
            grid[y][x] = 2
            convert_land(x-1, y)
            convert_land(x+1, y)
            convert_land(x, y-1)
            convert_land(x, y+1)
        
        for y in range(n):
            convert_land(0, y)
            convert_land(m-1, y)
        
        for x in range(m):
            convert_land(x, 0)
            convert_land(x, n-1)
            
        islands = 0
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == 0:
                    islands += 1
                    convert_land(x, y)
        return islands
        
