"""
29. Divide Two Integers
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.

Example 2:
Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.

Example 3:
Input: dividend = 0, divisor = 1
Output: 0

Example 4:
Input: dividend = 1, divisor = 1
Output: 1

Constraints:
-231 <= dividend, divisor <= 231 - 1
divisor != 0
"""
# Time complexity: O(log N)
# Space complexity: O(1)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        pos = (dividend >= 0) == (divisor >= 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i *= 2 # i <<= 1
                temp *= 2 # temp <<= 1
        return min(res if pos else -res, 2147483647)
    
"""
x << y
Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.

x >> y
Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.
"""
