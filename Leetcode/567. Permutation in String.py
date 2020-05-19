"""
567. Permutation in String
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""
# Time complexity: O(N), because comparing permutations of bounded elements is constant time
# Space complexity: O(1), because there are a maximum of 26 characters stored
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        size = len(s1)
        permutation = collections.Counter(s1)
        curr = collections.Counter()

        for i, c in enumerate(s2):
            curr[c] += 1
            
            if i >= size:
                curr[s2[i-size]] -= 1
                if curr[s2[i-size]] == 0:
                    del curr[s2[i-size]]
            
            if curr == permutation:
                return True

        return False
