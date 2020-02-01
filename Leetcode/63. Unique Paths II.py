"""
63. Unique Paths II
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2

Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""
# Time complexity: O(N*M)
# Space complexity: O(N)
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        n = len(grid[0])
        dp = [0 for _ in range(n)]
        dp[0] = 1
        for row in grid:
            for j, val in enumerate(row):
                if val == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j-1]
        return dp[-1]
