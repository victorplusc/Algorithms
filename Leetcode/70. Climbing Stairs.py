"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""

class Solution:
    def climbStairs(self, n):
        
        if n <= 2:
            return n

        first, second, curr = 1, 2, 0

        for step in range(2, n):
            curr = first + second
            first, second = second, curr

        return curr
