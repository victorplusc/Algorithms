"""
Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.constant_space(grid)
        return self.linear_space(grid)
        return self.two_dimensional(grid)
    
    # Time complexity: O(N*M)
    # Space complexity: O(N*M)
    def two_dimensional(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [[0 for x in range(n)] for y in range(m)]
        dp[0][0] = grid[0][0]
        for y in range(1, m): dp[y][0] = dp[y-1][0] + grid[y][0]
        for x in range(1, n): dp[0][x] = dp[0][x-1] + grid[0][x]
        for y in range(1, m):
            for x in range(1, n):
                dp[y][x] += grid[y][x] + min(dp[y-1][x], dp[y][x-1])
        return dp[-1][-1]


    # Time complexity: O(N*M)
    # Space complexity: O(N)
    def linear_space(self, grid):
        n = len(grid[0])
        dp = [0] + [float('inf') for _ in range(n-1)]
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if x == 0:
                    dp[x] += val
                else:
                    dp[x] = val + min(dp[x], dp[x-1])
        return dp[-1]


    # Time complexity: O(N*M)
    # Space complexity: O(1)
    def constant_space(self, grid):
        m, n = len(grid), len(grid[0])
        for y in range(1, m): grid[y][0] += grid[y-1][0]
        for x in range(1, n): grid[0][x] += grid[0][x-1]
        for y in range(1, m):
            for x in range(1, n):
                grid[y][x] += min(grid[y-1][x], grid[y][x-1])
        return grid[-1][-1]
