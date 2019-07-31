"""
1137. N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""
# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1 or n == 2: return 1
        
        t_0, t_1, t_2 = 0, 1, 1
        
        for i in range(n):
            t_n = t_0 + t_1 + t_2
            t_0, t_1, t_2 = t_1, t_2, t_n
        
        return t_0
