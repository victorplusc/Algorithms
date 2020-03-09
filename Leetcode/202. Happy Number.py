"""
202. Happy Number
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 
Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        # return self.naive(n)
        return self.floyd(n)
        
    def get_next(self, n):
        total_sum = 0
        while n > 0:
            d = n%10
            n //= 10
            total_sum += d*d
        return total_sum
    
    # Time complexity: O(log n)
    # Space complexity: O(log n)
    def naive(self, n):
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.get_next(n)
        return n == 1
    
    # Time complexity: O(log n)
    # Space complexity: O(1)
    def floyd(self, n):
        slow_runner = n
        fast_runner = self.get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = self.get_next(slow_runner)
            fast_runner = self.get_next(self.get_next(fast_runner))
        return fast_runner == 1
