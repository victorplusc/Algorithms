"""
6. ZigZag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""
# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
    
        n = len(s)
        rows = [""] * min(numRows, n)
        
        y = 0
        dy = 1
        for c in s:
            rows[y] += c
            y += dy
            if y == 0 or y == numRows-1:
                dy *= -1
                
        return "".join(["".join(row) for row in rows])
