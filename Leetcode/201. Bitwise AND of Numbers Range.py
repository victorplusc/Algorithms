"""
201. Bitwise AND of Numbers Range
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:
Input: [5,7]
Output: 4

Example 2:
Input: [0,1]
Output: 0
"""
# Time complexity: O(1)
# Space complexity: O(1)
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        return self.shifting(m, n)
        return self.kernighan(m, n)

    def shifting(self, m, n):
        shift = 0
        while m != n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift
    
    def kernighan(self, m, n):
        while m < n:
            n = n & (n-1)
        return m & n
