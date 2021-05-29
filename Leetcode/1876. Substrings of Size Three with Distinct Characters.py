"""
1876. Substrings of Size Three with Distinct Characters
A string is good if there are no repeated characters.

Given a string s, return the number of good substrings of length three in s.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

Example 1:
Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".

Example 2:
Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".

Constraints:
1 <= s.length <= 100
s consists of lowercase English letters.
"""
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        
        window = collections.Counter()
        substrs = len(window) == 3
        for i in range(len(s)):
            if i < 3:
                window[s[i]] += 1
            else:
                if s[i-3] in window:
                    window[s[i-3]] -= 1
                    if window[s[i-3]] == 0:
                        del window[s[i-3]]
                window[s[i]] += 1
            substrs += len(window) == 3
        return substrs
            
