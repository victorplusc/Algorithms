"""
562. Longest Line of Consecutive One in Matrix
Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.

Example:
Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
Output: 3
Hint: The number of elements in the given matrix will not exceed 10,000.
"""
class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        return self.dp_3d(M)
        return self.dp_2d(M)

    # Time complexity: O(N*M)
    # Space complexity: O(N*M)
    def dp_3d(self, M):
        if not M: return 0
        n, m = len(M), len(M[0])
        dp = [[[0] * 4 for k in range(m)] for _ in range(n)]
        ones = 0
        for y in range(n):
            for x in range(m):
                if M[y][x] == 1:
                    dp[y][x][0] = dp[y][x-1][0] + 1 if x > 0 else 1
                    dp[y][x][1] = dp[y-1][x][1] + 1 if y > 0 else 1
                    dp[y][x][2] = dp[y-1][x-1][2] + 1 if y > 0 and x > 0 else 1
                    dp[y][x][3] = dp[y-1][x+1][3] + 1 if y > 0 and x < (m-1) else 1
                    ones = max(ones, dp[y][x][0], dp[y][x][1], dp[y][x][2], dp[y][x][3])
        return ones
    
    # Time complexity: O(N*M)
    # Space complexity: O(N)
    def dp_2d(self, M):
        if not M: return 0
        n, m = len(M), len(M[0])
        dp = [[0] * 4 for k in range(m)]
        ones = 0
        for y in range(n):
            old = 0
            for x in range(m):
                if M[y][x] == 1:
                    dp[x][0] = dp[x-1][0] + 1 if x > 0 else 1
                    dp[x][1] = dp[x][1] + 1 if y > 0 else 1
                    prev = dp[x][2]
                    dp[x][2] = old+1 if y > 0 and x > 0 else 1
                    old = prev
                    dp[x][3] = dp[x+1][3] + 1 if y > 0 and x < (m-1) else 1
                    ones = max(ones, dp[x][0], dp[x][1], dp[x][2], dp[x][3])
                else:
                    old = dp[x][2]
                    dp[x][0] = dp[x][1] = dp[x][2] = dp[x][3] = 0
        return ones
