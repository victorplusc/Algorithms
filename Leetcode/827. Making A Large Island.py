"""
827. Making A Large Island
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

Example 1:
Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Example 2:
Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

Example 3:
Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.
"""
# Time complexity: O(N^2)
# Space complexity: O(N^2)
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        visited = set()
        zeros = set()
        island_sizes = collections.Counter()
        i = 2
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(y, x):
            if y < 0 or y >= n or x < 0 or x >= m or grid[y][x] != 1:
                return
            island_sizes[i] += 1
            grid[y][x] = i
            for dy, dx in directions:
                dfs(y+dy, x+dx)

        for y in range(n):
            for x in range(m):
                if grid[y][x] == 0:
                    zeros.add((y, x))
                else:
                    dfs(y, x)
                    i += 1
        
        max_island = 1
        for y, x in zeros:
            used_islands = set()
            curr = 1
            for dy, dx in directions:
                if y+dy < 0 or y+dy >= n or x+dx < 0 or x+dx >= m or grid[y+dy][x+dx] == 0 or grid[y+dy][x+dx] in used_islands:
                    continue
                used_islands.add(grid[y+dy][x+dx])
                curr += island_sizes[grid[y+dy][x+dx]]
            max_island = max(max_island, curr)
        return max_island if zeros else n*m
