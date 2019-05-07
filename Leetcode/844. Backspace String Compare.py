# 844. Backspace String Compare

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        string_s = []
        string_t = []
        
        for char in S:
            if char != "#":
                string_s.append(char)
            elif string_s != []:
                string_s.pop()
        
        for char in T:
            if char != "#":
                string_t.append(char)
            elif string_t != []:
                string_t.pop()
        
        return string_s == string_t
    
"""
Time complexity: O(N + M), N being the length of S, M being the length of T
Space complexity: O(N + M), N being the length of S, M being the length of T
"""
