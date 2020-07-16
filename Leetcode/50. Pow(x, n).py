"""
50. Pow(x, n)
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:
Input: 2.00000, 10
Output: 1024.00000

Example 2:
Input: 2.10000, 3
Output: 9.26100

Example 3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:
-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return self.recursive(x, n)
        return self.iterative(x, n)
    
    # Time complexity: O(log N)
    # Space complexity: O(1)
    def iterative(self, x, n):
        if n < 0:
            n *= -1
            x = 1/x
        
        output = 1
        curr_prod = x
        i = n
        while i > 0:
            if i%2 == 1:
                output *= curr_prod
            curr_prod = curr_prod*curr_prod
            i //= 2
        return output
        
    # Time complexity: O(log N)
    # Space complexity: O(log N)
    def recursive(self, x, n):
        def fast_power(x, n):
            if n == 0:
                return 1.0
            half = fast_power(x, n//2)
            if n % 2 == 0:
                return half*half
            else:
                return half*half*x   
        N = n
        if N < 0:
            x = 1/x
            N *= -1
        return fast_power(x, N)
