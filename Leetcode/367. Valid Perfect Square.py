"""
367. Valid Perfect Square
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
Input: 16
Output: true

Example 2:
Input: 14
Output: false
"""
# Time complexity: O(log N)
# Space complexity: O(1)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        x = num // 2
        while x**2 > num:
            x = (x + num//x) // 2
        return x**2 == num
