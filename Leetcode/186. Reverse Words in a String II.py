"""
186. Reverse Words in a String II
Given an input string , reverse the string word by word. 

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Note: 

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?
"""

# Time complexity: O(N)
# Space complexity: O(1)

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse_word(s, 0, len(s)-1)
        start = 0
        
        for end in range(len(s)):
            if s[end] == " ":
                self.reverse_word(s, start, end - 1)
                start = end + 1
            elif end == len(s)-1:
                self.reverse_word(s, start, end)
                
        
    def reverse_word(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        
        
        
