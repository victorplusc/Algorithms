"""
97. Interleaving String
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true

Constraints:
0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.

Follow up: Could you solve it using only O(s2.length) additional memory space?
"""
class Solution:
    # Time complexity: O(N*M)
    # Space complexity: O(N*M)
    def isInterleaveDP(self, s1: str, s2: str, s3: str) -> bool:
        n, m, k = len(s1), len(s2), len(s3)
        if n+m != k:
            return False
        
        dp = [[False]*(m+1) for _ in range(n+1)]
        # dp[n][m], down is s1, right is s2
        
        dp[0][0] = True
        for i in range(1, n+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
            
        for j in range(1, m+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1] or \
                dp[i][j-1] and s2[j-1] == s3[i+j-1]
        return dp[-1][-1]
    
    # BFS
    # Time complexity: O(N*M)
    # Space complexity: O(N*M)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, k = len(s1), len(s2), len(s3)
        if n+m != k:
            return False
        
        q = collections.deque([(0, 0)])
        visited = {(0, 0)}
        
        while q:
            x, y = q.popleft()
            if x+y == k:
                return True
            if y+1 <= n and s1[y] == s3[x+y] and (x, y+1) not in visited:
                q.append((x, y+1))
                visited.add((x, y+1))
            if x+1 <= m and s2[x] == s3[x+y] and (x+1, y) not in visited:
                q.append((x+1, y))
                visited.add((x+1, y))
        return False
