"""
1119. Remove Vowels from a String
Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

Example 1:

Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:

Input: "aeiou"
Output: ""
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def removeVowels(self, S: str) -> str:
        return "".join([c for c in S if c not in {"a", "e", "i", "o", "u"}])
