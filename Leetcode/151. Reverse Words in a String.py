"""
151. Reverse Words in a String
Given an input string, reverse the string word by word.

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
"""

# Time complexity: O(N)
# Space complexity: O(N)
class Solution(object):
    def reverseWords(self, s):
        if not s:
            return ""
        
        words = s.split()
        for i in range(len(words)//2):
            words[i], words[-1-i] = words[-1-i], words[i]
        return " ".join(words)
        

"""
    def reverseWords(self, s):
        if not s:
            return ""
        
        chars = [i for i in s]
        self.reverse_from_index(chars, 0, len(chars)-1)
        start = 0
        
        for i in range(len(chars)):
            if chars[i] == " ":
                self.reverse_from_index(chars, start, i-1)
                start = i+1
            elif i+1 == len(chars):
                self.reverse_from_index(chars, start, i)

        return "".join(chars)
    
    def reverse_from_index(self, chars, start, end):
        while start < end:
            chars[start], chars[end] = chars[end], chars[start]
            start += 1
            end -= 1
"""
