"""
329. Longest Increasing Path in a Matrix
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:
Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""
# Time complexity: O(N*M)
# Space complexity: O(N*M)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        self.dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        longest = 0
        
        for y in range(m):
            for x in range(n):
                longest = max(longest, self.dfs(matrix, y, x, dp))
        return longest
    
    def dfs(self, matrix, y, x, dp):
        if dp[y][x]: return dp[y][x]
        
        for a, b in self.dirs:
            r, c = y+a, x+b
            if 0 <= c < len(matrix[0]) and 0 <= r < len(matrix) and matrix[r][c] > matrix[y][x]:
                dp[y][x] = max(dp[y][x], self.dfs(matrix, r, c, dp))
        
        dp[y][x] += 1
        return dp[y][x]
