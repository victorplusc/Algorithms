"""
266. Palindrome Permutation
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
"""
# Time complexity: O(N)
# Space complexity: O(1)
import collections
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        mapping = [0 for _ in range(128)]
        count = 0
        for i in range(len(s)):
            mapping[ord(s[i])] += 1
            if mapping[ord(s[i])] % 2 == 0:
                count -= 1
            else:
                count += 1
        return count <= 1
