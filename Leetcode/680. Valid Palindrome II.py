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
        def is_palin(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        n = len(s)
        
        for i in range(n):
            if s[i] != s[~i]:
                return is_palin(i+1, n-1-i) or is_palin(i, n-2-i)
            
        return True
