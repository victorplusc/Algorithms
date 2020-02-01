"""
62. Unique Paths
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""
class Solution(object):
    def uniquePaths(self, m, n):
        # return self.two_dimensional(m, n)
        return self.space_optimized(m, n)
    
    # Time complexity: O(N*M)
    # Space complexity: O(N)
    def space_optimized(self, m, n):
        if not m or not n: return 0
        
        dp = [1 for _ in range(n)]
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]

        return dp[-1]
    
    # Time complexity: O(N*M)
    # Space complexity: O(N*M)
    def two_dimensional(self, m, n):
        grid = [[1 for i in range(n)] for i in range(m)]
        
        for y in range(1, m):
            for x in range(1, n):
                grid[y][x] = grid[y-1][x] + grid[y][x-1]
                
        return grid[-1][-1]
