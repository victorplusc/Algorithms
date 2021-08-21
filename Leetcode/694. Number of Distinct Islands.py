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
        m = len(grid)
        n = len(grid[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(x, y, x_change=0, y_change=0):
            nonlocal order
            if x < 0 or y < 0 or x >= n or y >= m or grid[y][x] != 1:
                return
            grid[y][x] = 2 # marks cell as visited
            order.append((x_change, y_change))
            order.append(str(x_change)+"y"+str(y_change))
            for dy, dx in directions:
                dfs(x+dx, y+dy, x_change+dx, y_change+dy)

        islands = set()
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == 1:
                    order = []
                    dfs(x, y)
                    islands.add(tuple(order))

        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == 2:
                    grid[y][x] = 1

        return len(islands)
