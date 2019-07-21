"""
509. Fibonacci Number
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.
"""
# Time complexity: O(N)
# Space complexity: O(N)

class Solution:
    def fib(self, N: int) -> int:
        observed = {}
        return self.fib_helper(N, observed)
        
    def fib_helper(self, N: int, observed: dict) -> int:
        if N in {1, 2}:
            return 1
        elif N == 0:
            return 0
        
        if N not in observed:
            observed[N] = self.fib_helper(N-1, observed) + self.fib_helper(N-2, observed)
        
        return observed[N]
