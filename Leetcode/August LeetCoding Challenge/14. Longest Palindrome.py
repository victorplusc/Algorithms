"""
Longest Palindrome
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:
Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(s)
        one_off = True
        ans = 0
        
        for v in counter:
            if counter[v]%2 == 0:
                ans += counter[v]
            elif one_off:
                ans += counter[v]
                one_off = False
            elif counter[v] > 2:
                ans += counter[v]-1
        
        return ans
