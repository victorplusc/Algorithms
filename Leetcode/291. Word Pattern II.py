"""
291. Word Pattern II
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Example 1:
Input: pattern = "abab", str = "redblueredblue"
Output: true

Example 2:
Input: pattern = "aaaa", str = "asdasdasdasd"
Output: true

Example 3:
Input: pattern = "aabb", str = "xyzabcxzyabc"
Output: false

Constraints:
You may assume both pattern and str contains only lowercase letters.
"""
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def helper(i, j, ptable, stable):
            if i == len(pattern) and j == len(s):
                return True
            elif i == len(pattern) or j == len(s):
                return False
            else:
                p, added = pattern[i], False
                for k in range(j, len(s)):
                    word = s[j:k+1]
                    if (p in ptable and ptable[p] != word) or (word in stable and stable[word] != p):
                        continue
                    if p not in ptable and word not in stable:
                        ptable[p], stable[word], added = word, p, True
                    remainder = helper(i+1, k+1, ptable, stable)
                    if added:
                        del ptable[p]
                        del stable[word]
                    if remainder:
                        return True
        
        return helper(0, 0, {}, {})
