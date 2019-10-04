"""
168. Excel Sheet Column Title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
"""

# Time complexity: O(N)
# Space complexity: O(N)
import collections

class Solution:
    def convertToTitle(self, n: int) -> str:
        col = collections.deque()
        letters = [chr(ord("A")+i) for i in range(26)]
        
        while n > 0:
            col.appendleft(letters[n%26-1])
            n = (n-1)//26
            
        return "".join(col)
