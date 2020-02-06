"""
91. Decode Ways
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        # return self.dp(s)
        return self.constant_space(s)
    
    # Time complexity: O(N)
    # Space complexity: O(N)
    def dp(self, s):
        if not s:
            return 0
        n = len(s)
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1 if s[0] != "0" else 0
        for i in range(2, n+1):
            first = int(s[i-1:i])
            second = int(s[i-2:i])
            if 1 <= first <= 9:
                dp[i] += dp[i-1]
            if 10 <= second <= 26:
                dp[i] += dp[i-2]
        return dp[n]

    # Time complexity: O(N)
    # Space complexity: O(1)
    def constant_space(self, s):
        if not s:
            return 0
        n = len(s)
        second = 1
        first = 1 if s[0] != "0" else 0
        for i in range(2, n+1):
            single = int(s[i-1:i])
            double = int(s[i-2:i])
            curr = 0
            if single != 0:
                curr += first
            if 10 <= double <= 26:
                curr += second
            second, first = first, curr
        return first
