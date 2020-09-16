"""
58. Length of Last Word
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:
Input: "Hello World"
Output: 5
"""
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        length = 0
        for i in reversed(range(len(s))):
            if s[i] != " ":
                length += 1
            elif length > 0:
                return length
        return length
