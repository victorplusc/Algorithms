"""
420. Strong Password Checker
A password is considered strong if below conditions are all met:

It has at least 6 characters and at most 20 characters.
It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
Write a function strongPasswordChecker(s), that takes a string s as input, and return the MINIMUM change required to make s a strong password. If s is already strong, return 0.

Insertion, deletion or replace of any one character are all considered as one change.
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        missing_lower = missing_upper = missing_digit = True
        for c in s:
            if c.islower(): missing_lower = False
            if c.isupper(): missing_upper = False
            if c.isdigit(): missing_digit = False
        missing = missing_lower + missing_upper + missing_digit
        
        n = len(s)
        if n < 6:
            return max(missing, 6-n)
        
        replacements = 0
        one_del = 0
        two_del = 0
        i = 2
        while i < n:
            if s[i] == s[i-1] == s[i-2]:
                length = 2
                while i < n and s[i] == s[i-1]:
                    length += 1
                    i += 1
                replacements += length//3
                if length%3 == 0:
                    one_del += 1
                elif length%3 == 1:
                    two_del += 1
            else:
                i += 1
                
        if n <= 20: 
            return max(missing, replacements)
        else:
            del_count = n-20
            replacements -= min(del_count, one_del)
            replacements -= min(max(del_count - one_del, 0), two_del*2)//2
            replacements -= max(del_count-one_del-2*two_del, 0)//3
            return del_count + max(missing, replacements)
        
