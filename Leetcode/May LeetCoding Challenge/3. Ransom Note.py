"""
Ransom Note
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""
# Time complexity: O(N+M)
# Space complexity: O(N+M)
class Solution:
    def canConstruct(self, ransom_note: str, magazine: str) -> bool:
        required = collections.Counter(ransom_note)
        available = collections.Counter(magazine)
        for c in required:
            if c not in available or required[c] > available[c]:
                return False
        return True
