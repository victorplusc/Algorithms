"""
459. Repeated Substring Pattern
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:
Input: "aba"
Output: False

Example 3:
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

Let S be the input string and Sb be each substring:

S = SbSb, when S has two repeatable patterns.
SS = SbSbSbSb

By removing the first and last characters of SS, we generate:

X = SnSbSbSm

If there exists a repeatable pattern, S will be in X.
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        rotated = (2*s)[1:-1]
        return s in rotated
