"""
1143. Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # return self.classic(text1, text2)
        return self.linear_space(text1, text2)
    
    # Time complexity: O(M*N)
    # Space complexity: O(M*N)
    def classic(self, text1, text2):
        n, m = len(text1), len(text2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                dp[i+1][j+1] = dp[i][j]+1 if text1[i] == text2[j] else max(dp[i+1][j], dp[i][j+1])
        return dp[-1][-1]

    # Time complexity: O(M*N)
    # Space complexity: O(min(M, N))   
    def linear_space(self, text1, text2):
        if len(text2) < len(text1):
            text1, text2 = text2, text1
        
        # Text 1 will always be the shortest
        prev = [0] * (len(text1)+1)
        curr = [0] * (len(text1)+1)
        
        for y in reversed(range(len(text2))):
            for x in reversed(range(len(text1))):
                if text2[y] == text1[x]:
                    curr[x] = 1 + prev[x+1]
                else:
                    curr[x] = max(prev[x], curr[x+1])
            prev, curr = curr, prev
        
        return prev[0]
