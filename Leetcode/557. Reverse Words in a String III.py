"""
Given a string, you need to reverse the order of characters in each word
within a sentence while still preserving whitespace and initial word order.
"""
#Example:
    #Input: "Let's take LeetCode contest"
    #Output: "s'teL ekat edoCteeL tsetnoc"

class Solution:
    def reverseWords(self, s: str) -> str:
        words = list(s)
        start = end = 0
        
        while start < len(s):
            if end+1 == len(s):
                self.reverse_word(words, start, end)
                break
            elif words[end] == " ":
                self.reverse_word(words, start, end-1)
                start = end + 1
            end += 1
                
        return "".join(words)
        
    def reverse_word(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

#Time complexity: O(N)
#Space complexity: O(1), if in a language where the string is mutable, else O(N)
