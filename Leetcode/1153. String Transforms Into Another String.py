"""
1153. String Transforms Into Another String
Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 by doing zero or more conversions.

In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.

Return true if and only if you can transform str1 into str2.

Example 1:
Input: str1 = "aabcc", str2 = "ccdee"
Output: true
Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.

Example 2:
Input: str1 = "leetcode", str2 = "codeleet"
Output: false
Explanation: There is no way to transform str1 to str2.

Note:
1 <= str1.length == str2.length <= 10^4
Both str1 and str2 contain only lowercase English letters.
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def canConvert(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        n = len(s1)
        mapping = {}
        for i in range(n):
            c1, c2 = s1[i], s2[i]
            if c1 in mapping and mapping[c1] != c2:
                return False
            mapping[c1] = c2
        return len(set(s2)) < 26
