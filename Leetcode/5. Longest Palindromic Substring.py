"""
5. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

# Time complexity: O(N**2)
# Space complexity: O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "": return ""
        
        start = end = 0
        for i in range(len(s)):
            len1 = self.expand_around_center(s, i, i)
            len2 = self.expand_around_center(s, i, i+1)
            max_len = max(len1, len2)
            if max_len > end-start:
                start = i - (max_len-1)//2
                end = i + 1 + max_len//2

        return s[start:end]
    
    def expand_around_center(self, s, L, R):
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R-L-1
