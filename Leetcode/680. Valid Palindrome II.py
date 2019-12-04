"""
680. Valid Palindrome II
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)//2):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                return self.valid_palin_range(s, i+1, j) or self.valid_palin_range(s, i, j-1)
        return True
    
    def valid_palin_range(self, s, i, j):
        return all(s[k] == s[j-k+i] for k in range(i, j))
