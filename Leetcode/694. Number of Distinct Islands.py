"""
694. Number of Distinct Islands
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.

Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.
"""
# Time complexity: O(N*M)
# Space complexity: O(N*M)
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        return self.shape_hash(grid)
        return self.path_hash(grid)
    
    def path_hash(self, grid):
        seen = set()
        def dfs(y, x, di):
            if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] and (y, x) not in seen:
                seen.add((y, x))
                shape.append(di)
                dfs(y+1, x, 1)
                dfs(y-1, x, 2)
                dfs(y, x+1, 3)
                dfs(y, x-1, 4)
                shape.append(0)
        
        shapes = set()
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    shape = []
                    dfs(y, x, 0)
                    if shape:
                        shapes.add(tuple(shape))
        return len(shapes)
    
    def shape_hash(self, grid):
        seen = set()
        def dfs(y, x, y0, x0):
            if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] and (y, x) not in seen:
                seen.add((y, x))
                shape.add((y-y0, x-x0))
                dfs(y+1, x, y0, x0)
                dfs(y-1, x, y0, x0)
                dfs(y, x+1, y0, x0)
                dfs(y, x-1, y0, x0)
        
        shapes = set()
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    shape = set()
                    dfs(y, x, y, x)
                    if shape:
                        shapes.add(frozenset(shape))
        return len(shapes)
