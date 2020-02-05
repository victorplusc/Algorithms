"""
32. Longest Valid Parentheses
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # return self.dp(s)
        # return self.stack(s)
        return self.two_passes(s)

    # Time complexity: O(N)
    # Space complexity: O(N)
    def dp(self, s):
        if len(s) <= 1:
            return 0
        longest = 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = dp[i-2] + 2 if (i-2 > 0) else 2
                    longest = max(dp[i], longest)
                else:
                    if i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == "(":
                        dp[i] = dp[i-1] + 2 + (dp[i-dp[i-1]-2] if i-dp[i-1]-2 >= 0 else 0)
                        longest = max(dp[i], longest)
        return longest
        
    # Time complexity: O(N)
    # Space complexity: O(N)
    def stack(self, s):
        longest = 0
        stack = [0]
        for i, c in enumerate(s):
            if c == "(":
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val+2
                    longest = max(longest, stack[-1])
                else:
                    stack = [0]
        return longest
    
    # Time complexity: O(N)
    # Space complexity: O(1)
    def two_passes(self, s):
        n = len(s)
        if n <= 1:
            return 0
        left = right = longest = 0
        
        for c in s:
            if c == "(":
                left += 1
            else:
                right += 1
            if left == right:
                longest = max(longest, 2*left)
            elif right > left:
                left = right = 0
        
        right = left = 0
        for i in range(n-1, 0, -1):
            if s[i] == ")":
                right += 1
            else:
                left += 1
            if left == right:
                longest = max(longest, 2*right)
            elif left > right:
                right = left = 0
        return longest
