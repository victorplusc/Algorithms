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
        def reverse_partial(left, right):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
                
        reverse_partial(0, len(s)-1)
        i = 0
        for j in range(len(s)):
            if s[j] == " ":
                reverse_partial(i, j-1)
                
                i = j+1
        reverse_partial(i, len(s)-1)
    
        
        
        
