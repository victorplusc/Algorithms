"""
583. Delete Operation for Two Strings

Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # return self.memoized(word1, word2)
        # return self.non_lcs(word1, word2)
        return self.lcs(word1, word2)
        return self.lcs_space_optimzied(word1, word2)
    
    
    # Time complexity: O(N*M)
    # Space complexity: O(N*M)
    def non_lcs(self, word1, word2):
        n, m = len(word1), len(word2)
        
        dp = [[0] * (m+1) for i in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = i
        
        for j in range(m+1):
            dp[0][j] = j
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
    
    # Time complexity: O(N*M)
    # Space complexity: O(min(N, M))
    def lcs_space_optimzied(self, word1, word2):
        if len(word1) > len(word2):
            word1, word2 = word2, word1
            
        n, m = len(word1), len(word2)
        
        dp = [0 for i in range(n+1)]
        
        for y in range(m):
            temp = [0] * (n+1)
            for x in range(n):
                if word2[y] == word1[x]:
                    temp[x+1] = 1 + dp[x]
                else:
                    temp[x+1] = max(dp[x+1], temp[x])
            dp = temp
        return n+m - 2*dp[-1]
    
    # Time complexity: O(N*M)
    # Space complexity: O(N*M)
    def lcs(self, word1, word2):
        n, m = len(word1), len(word2)
        
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        for i in range(n):
            for j in range(m):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return n+m - 2*dp[-1][-1]
    
    # Time complexity: O(N*M)
    # Space complexity: O(N*M)
    def memoized(self, word1, word2):
        n, m = len(word1), len(word2)        
        memo = [[0]*(m+1) for _ in range(n+1)]
        return n+m - 2*self.helper(word1, word2, n, m, memo)
        
    def helper(self, word1, word2, n, m, memo):
        if n == 0 or m == 0:
            return 0
        if memo[n][m] > 0:
            return memo[n][m]
        if word1[n-1] == word2[m-1]:
            memo[n][m] = 1 + self.helper(word1, word2, n-1, m-1, memo)
        else:
            memo[n][m] = max(self.helper(word1, word2, n-1, m, memo), self.helper(word1, word2, n, m-1, memo))
        return memo[n][m]
    
