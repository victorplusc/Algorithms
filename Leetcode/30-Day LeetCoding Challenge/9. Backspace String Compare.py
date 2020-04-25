"""
Backspace String Compare
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:
1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.

Follow up:
Can you solve it in O(N) time and O(1) space?
"""
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.naive(S, T)
        return self.two_pointers(S, T)
    
    # Time complexity: O(N)
    # Space complexity: O(1)
    def two_pointers(self, s, t):
        i = len(s)-1
        j = len(t)-1
        s_del = 0
        t_del = 0
        
        while True:
            while i >= 0 and (s_del or s[i] == "#"):
                if s[i] == "#":
                    s_del += 1
                else:
                    s_del -= 1
                i -= 1
            while j >= 0 and (t_del or t[j] == "#"):
                if t[j] == "#":
                    t_del += 1
                else:
                    t_del -= 1
                j -= 1
            if not (i >= 0 and j >= 0 and s[i] == t[j]):
                return i == j == -1
            i -= 1
            j -= 1
        return True
    
    # Time complexity: O(N)
    # Space complexity: O(N)
    def naive(self, S, T):
        s = []
        t = []
        
        for c in S:
            if c == "#" and s:
                s.pop()
            elif c != "#":
                s.append(c)
        
        for c in T:
            if c == "#" and t:
                t.pop()
            elif c != "#":
                t.append(c)
        
        return s == t
