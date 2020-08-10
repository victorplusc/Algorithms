"""
Excel Sheet Column Number
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
    
Example 1:
Input: "A"
Output: 1

Example 2:
Input: "AB"
Output: 28

Example 3:
Input: "ZY"
Output: 701
"""
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def titleToNumber(self, s: str) -> int:
        mapping = {chr(ord("A")+i) : i+1 for i in range(26)}
    
        n = 0
        size = len(s)-1
        for i, c in enumerate(s):
            n += mapping[c] * 26**(size-i)
        
        return n
