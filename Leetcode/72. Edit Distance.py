"""
72. Edit Distance
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5

Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""
# Time complexity: O(N*M)
# Space complexity: O(N*M)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        
        if n*m == 0:
            return n+m
        
        d = [[0] * (m+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            d[i][0] = i
        
        for j in range(1, m+1):
            d[0][j] = j
            
        for i in range(1, n+1):
            for j in range(1, m+1):
                left = d[i-1][j] + 1
                down = d[i][j-1] + 1
                diag = d[i-1][j-1]
                if word1[i-1] != word2[j-1]:
                    diag += 1
                d[i][j] = min(left, down, diag)
        return d[n][m]
