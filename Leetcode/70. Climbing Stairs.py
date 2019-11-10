"""
70. Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""

class Solution:
    # Time complexity: O(N)
    # Space complexity: O(N)
    def climbStairs(self, n):
        self.memo = {}
        return self.helper(0, n)
    
    def helper(self, step, n):
        if step > n:
            return 0
        if step == n:
            return 1
        
        if step in self.memo:
            return self.memo[step]
        else:
            self.memo[step] = self.helper(step + 1, n) + self.helper(step + 2, n)
        
        return self.memo[step]
    
    # Time complexity: O(N)
    # Space complexity: O(1)
    def climbStairs(self, n):
        if n <= 0: return 0
        if n in {1, 2}:
            return n
        one_behind = 2
        two_behind = 1
        total = 0
    
        for i in range(2, n):
            total = one_behind + two_behind
            two_behind = one_behind
            one_behind = total
        return total
