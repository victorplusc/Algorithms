"""
Detect Capital
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:
Input: "USA"
Output: True

Example 2:
Input: "FlaG"
Output: False

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if not word: return True
        
        n = len(word)
        
        lowercases = 0
        uppercases = 0
        
        lower = {chr(ord("a")+i) for i in range(26)}
        upper = {chr(ord("A")+i) for i in range(26)}
        
        capitalized = word[0] in upper
        
        for i in range(1, n):
            if word[i] in lower:
                lowercases += 1
            if word[i] in upper:
                uppercases += 1
        
        if lowercases == n-1:
            return True
        elif capitalized and lowercases > 0:
            return False
        elif capitalized and uppercases == n-1:
            return True
        return False
