"""
383. Ransom Note
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""
# Time complexity: O(N+M)
# Space complexity: O(1), worst case is max(N,M) == 26
import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_chars = collections.Counter(ransomNote)
        magazine_chars = collections.Counter(magazine)
        for c in ransom_chars:
            if c not in magazine_chars or ransom_chars[c] > magazine_chars[c]:
                return False
        return True
