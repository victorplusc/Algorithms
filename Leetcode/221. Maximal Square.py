"""
221. Maximal Square
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:
Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""
# Time complexity: O(N*M)
# Space complexity: O(N)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [0 for y in range(n+1)]
        max_sq = 0
        prev = 0
        for y in range(m):
            for x in range(n):
                temp = dp[x+1]
                if matrix[y][x] == "1":
                    dp[x+1] = min(dp[x], prev, dp[x+1])+1
                    max_sq = max(dp[x+1], max_sq)
                else:
                    dp[x+1] = 0
                prev = temp
        return max_sq**2
